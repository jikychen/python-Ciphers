# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 09:48:35 2018

@author: jikychen
"""
import time, os, sys

def main():
    inputFilename = 'frankenstein.txt'
    outputFilename = 'frankenstein.encrypt.txt'
    myKey = 10
    myMode = 'encrypt'
    
    if not os.path.exists(inputFilename):
        print('The file %s dose not exist. Quitting...' % (inputFilename))
        sys.exit()
    
    fileObj = open(inputFilename)
    content = ''
    Msg = fileObj.read(20)
    while len(Msg) > 0:
        content = content + Msg
        Msg = fileObj.read(20)
    fileObj.close()
    
    print(content)
    
if __name__ == '__main__':
    main()