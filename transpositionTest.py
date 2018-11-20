# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:57:23 2018

@author: jikychen
"""

#Transposition Cipher Test
import random, sys, transpositionEncrypt, transpositionDecrypt
def main():
    random.seed(40)
    
    for i in range(20):
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)
        
        print('Test #%s: "%s..."' % (i+1, message[:50]))
        
        for key in range(1, len(message)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted) 
            if message != decrypted:
                print('Mismatch with key %s and message %s.' %(key, message))
                print(decrypted)
                sys.exit()

    print('Transposition cipher test passed.')
    
if __name__ == '__main__':
    main()