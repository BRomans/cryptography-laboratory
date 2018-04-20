# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 10:20:53 2018

@author: Michele Romani


ENCRYPT THEN MAC
"""

import sys
import binascii
import os
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

block = algorithms.AES.block_size/8

filename = input('Type the file to encrypt: ')
with open(filename, 'rb') as f:
    plaintext = f.read()
#if len(plaintext) % block != 0:
    #sys.exit('The file must be multiple of ' + str(block) + ' bytes.')

key_hex_16 = input('Type the key in ' + str(block) + ' hexadecimal digits: ')
key16 = binascii.unhexlify(key_hex_16)
key_hex_32 = input('Type the key in ' + str(2*block) + ' hexadecimal digits: ')
key32 = binascii.unhexlify(key_hex_32)

iv = os.urandom(block)

ctx = hmac.HMAC(key32, hashes.SHA256(), default_backend())

for line in f:
    ctx.update(line)
digest1 = ctx.finalize()
#cipher = Cipher(algorithms.AES(key32), modes.CBC(iv), default_backend())
#ctx = cipher.encryptor()
#ciphertext = ctx.update(plaintext) + ctx.finalize()

#with open(filename + '.enc', 'wb') as f:
 #   f.write(iv)
  #  f.write(ciphertext)
#print('Encrypted file: ' + filename + '.enc')