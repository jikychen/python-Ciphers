# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 08:48:17 2018

@author: jikychen
"""

#transpositionDecrypt
import math, pyperclip

def tranString(string): #将练习中的(s)替换成空格
    sub = '(s)'
    while string.find(sub) != -1:
        string = string[:string.find(sub)] + ' ' + string[string.find(sub)+3:]
    return string

def main():
    myMessage = tranString(input('Input the message:'))
    myKey = int(input('Input the key:'))
    
    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext)
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    numOfCol = math.ceil(len(message) / key)
    numOfRow = key
    numOfShadedBoxes = numOfCol * numOfRow - len(message)
    
    plaintext = [''] * numOfCol
    
    col = 0
    row = 0
    
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == numOfCol) or (col == numOfCol - 1 and row >= numOfRow - numOfShadedBoxes):
            col = 0
            row += 1
    
    return ''.join(plaintext)


if __name__ == '__main__':
    main()
    