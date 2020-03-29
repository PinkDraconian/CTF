#!/usr/bin/env python

import time
import base64
from hashlib import md5
from Crypto.Cipher import AES


def main():
	padding = '\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
	with open('encrypted') as file:
		encrypted = base64.b64decode(file.readline())
	wanted_enc = encrypted[-16:]

	current_time = int(time.time())
	prev_time = current_time - 60 * 60 * 24 * 3
	for i in range(prev_time, current_time):
		print('[{}] Trying...'.format(i))
		key = md5(str(i)).digest()
		aes = AES.new(key, AES.MODE_ECB)
		out_data = aes.encrypt(padding)
		if out_data == wanted_enc:
			print('FLAG: {}'.format(aes.decrypt(encrypted)))
			break


if __name__ == '__main__':
	main()
