#!/usr/bin/env python

from pwn import *


def all_possible_triangles(n):
	""" Calculates the amount of possible triangles without looping through all combinations"""
	count = 0
	adder = 1
	prev = 0
	switch = 2
	for i in range(4, n + 1):
		prev += adder
		count += prev
		switch -= 1
		if switch <= 0:
			switch = 2
			adder += 1
	return count


def main():
	conn = remote('15.164.75.32', 1999)
	
	conn.recvuntil('n = ')
	n = int(conn.recvline())
	print(n)
	count = all_possible_triangles(n)
	conn.sendline(str(count))

	print(conn.recvuntil('n = '))
	n = int(conn.recvline())
	print(n)
	count = all_possible_triangles(n)
	conn.sendline(str(count))

	print(conn.recvuntil('n = '))
	n = int(conn.recvline())
	print(n)
	count = all_possible_triangles(n)
	conn.sendline(str(count))

	conn.recv()
	print(conn.recv())


if __name__ == "__main__":
    main()
