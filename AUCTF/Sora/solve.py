#!/usr/bin/env python3

def main():
	secrets = [ord(i) for i in 'aQLpavpKQcCVpfcg']
	solution = ''
	for secret in secrets:
		for i in range(255):
			if (i * 8 + 0x13) % 0x3d + 0x41 == secret:
				solution += chr(i)
				break
	print(solution)


if __name__ == '__main__':
	main()
