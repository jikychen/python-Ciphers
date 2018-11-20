# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:13:16 2018

@author: jikychen
"""

#Caesar Cipher Hacker
message = input('Input the code:')
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#加密和解密用的字母表必须一致
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num + key
            #选择加还是减，在加密和解密过程中要对应。
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Key #%s: %s' %(key,translated))
        