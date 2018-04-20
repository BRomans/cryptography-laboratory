# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 20:38:51 2017

@author: Pericle
"""

import binascii
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Cipher block size, expressed in bytes.
block = algorithms.AES.block_size/8

# Read the plaintext file.
filename = raw_input('Type the file to encrypt: ')
with open(filename, 'rb') as f:
    plaintext = f.read()

# Read the key in hexadecimal digits from keyboard.
key_hex = raw_input('Type the key in ' + str(2*block) + ' hexadecimal digits: ')
key = binascii.unhexlify(key_hex)

# Pad the plaintext to make it multiple of the block size.
ctx = padding.PKCS7(8*block).padder()
padded_plaintext = ctx.update(plaintext) + ctx.finalize()

# Encrypt the plaintext with a random IV.
iv = os.urandom(block)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
ctx = cipher.encryptor()
ciphertext = ctx.update(padded_plaintext) + ctx.finalize()

# Write the IV and the ciphertext in the output file.
with open(filename + '.enc', 'wb') as f:
    f.write(iv)
    f.write(ciphertext)
print('Encrypted file: ' + filename + '.enc')
