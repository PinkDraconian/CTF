#!/usr/bin/env python3

import os

enc_flag = ['0x2135d36aa0c278', '0x3e8f43212dafd7', '0x7a240c1672358', '0x37677cfb281b26', '0x26f90fe5a4bed0', '0xb0e1c482daf4', '0x59c069723a4e4b', '0x8cec977d4159']

flag = ''.join([os.popen('/root/ProgramFiles/RsaCtfTool/RsaCtfTool.py --publickey key.pub --uncipher ' + enc).read()[-6:-2:] for enc in enc_flag])
flag = flag.replace('\\x02', os.popen('/root/ProgramFiles/RsaCtfTool/RsaCtfTool.py --publickey key.pub --uncipher ' + enc_flag[-1]).read()[-12:-10:])
print(flag)
