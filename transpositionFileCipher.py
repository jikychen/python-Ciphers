# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 08:23:13 2018

@author: jikychen
"""

import time, os, sys, transpositionEncrypt, transpositionDecrypt
def tranString(string): #将练习中的\n替换成空格
    sub = '\n'
    while string.find(sub) != -1:
        string = string[:string.find(sub)] + ' ' + string[string.find(sub)+2:]
    return string

def main():
    inputFilename = 'frankenstein.txt'
    outputFilename = 'frankenstein.encrypt.txt'
    myKey = 10
    myMode = 'encrypt'
    
    if not os.path.exists(inputFilename):
        print('The file %s dose not exist. Quitting...' % (inputFilename))
        sys.exit()
        
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
        response = input('>')
        if not response.lower().startswith('c'):
            sys.exit()
    
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()
    
    content = tranString(content)
    print(content)
    print('%sing...' %(myMode.title()))
    
    starttime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - starttime, 2)
    print('%stion time: %s seconds' % (myMode.title(), totalTime))
    
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()
    
    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))
    
if __name__ == '__main__':
    main()
    
    