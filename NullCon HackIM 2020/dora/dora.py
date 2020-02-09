#!/usr/bin/env python3

from PIL import Image
from pwn import *


def find_skin_color_pixels():
    """Opens 'picture_out.png' and finds the kwadrant in which skin color pixels are found or returns -1 when no pixels where found"""
    r_min, r_max = 215, 230  # r skin color range
    g_min, g_max = 140, 160  # g skin color range
    b_min, b_max = 60, 80  # b skin color range

    img = Image.open('picture_out.png')  # Open image
    rgb = img.convert('RGB')  # Convert image to rgb
    pixel = 0  # Initialize pixel variable with value 0
    background = rgb.getpixel((0, 0))  # Cet the background color, used for making sure the program doesn't detect background pixels
    for x in range(img.size[0]):  # Loop through all pixels of the image
        for y in range(img.size[1]):
            r, g, b = rgb.getpixel((x, y))  # Get color at this position
            # If the color is between the defined skin color ranges and not the background
            if r_min <= r <= r_max and b_min <= b <= b_max and g_min <= g <= g_max and (r, g, b) != background:
                pixel = (x, y)  # Set our pixel to this position
                break  # Break because we found a skin color pixel

    if pixel == 0:  # If this is still zero, it means no skin color pixel was found
        return -1
    rx, ry = pixel  # Get position of our pixel
    mx, my = (img.size[0] / 2, img.size[1] / 2)  # Get center position of our image
    if rx < mx and ry < my:  # If in left upper kwadrant
        return 2
    elif rx < mx and ry > my:  # If in left lower kwadrant
        return 3
    elif rx > mx and ry < my:  # If in right upper kwadrant
        return 1
    elif rx > mx and ry > my:  # If in right lower kwadrant
        return 4
    return -1  # If at this point it hasn't returned yet, something went wrong so we just return not found to be safe


def main():
    count = 0  # Initialize a count variable used for showing the user how far we've made it
    conn = remote('misc.ctf.nullcon.net', 8000)  # Make a connection with the server
    conn.recvline(timeout=5)  # Info line on Dora
    base_png = conn.recvline(timeout=5)  # Get our image as b64
    done = False  # Variable used for ending the program in a proper fashion
    while not done:
        png = base64.b64decode(base_png)  # Decode the received b64
        with open('picture_out.png', 'wb') as f:  # Save the image we just got
            f.write(png)
        count += 1 
        result = find_skin_color_pixels()  # Find kwadrant in which there are skin color pixels
        if result == -1:  # If it returned -1, we need the user to identify it
            answer = input(str(count) + ': Enter 1, 2, 3 or 4: ').strip()  # Ask the user for the correct answer, note the strip to remove the newline at the end of user input
        else:  # If using the skin color, a kwadrant was found
            answer = str(result)  # Set that kwadrant to the answer
        conn.sendline(answer)  # Send our answer
        newline = conn.recvline(timeout=5)  # Server send back a newline
        base_png = conn.recvline(timeout=5)  # Followed by a new picture
        if newline != b'\n' or len(base_png) < 500:  # If the expected newline wasn't a newline or the b64 wasn't long enough, something unexpected happened
            print(newline)
            print(base_png)
            done = True  # The script can't recover from this so we set done to True
    conn.interactive()  # We move into interactive mode if the script has finished


if __name__ == '__main__':
    main()
