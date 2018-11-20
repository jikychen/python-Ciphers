# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:22:17 2018

@author: jikychen
"""

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')
    pyperclip.copy(ciphertext)
    
    
def encryptMessage(key, message):
    ciphertext = [''] * key #按照key的值复制字符串类型的列表项，否则在后面赋值时会超出列表长度。
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)
    #使用‘’（空字符）将ciphertext里面每个列表项连接起来
    
if __name__ == '__main__':
    main()