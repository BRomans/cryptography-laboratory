# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 20:38:51 2017

@author: Pericle
"""

import sys
import binascii
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Cipher block size, expressed in bytes.
block = algorithms.AES.block_size/8

# Read the IV and the ciphertext from a file.
filename = raw_input('Type the file to decrypt: ')
with open(filename, 'rb') as f:
    iv = f.read(block)
    ciphertext = f.read()
if len(ciphertext) % block != 0:
    sys.exit('The file must be multiple of ' + str(block) + ' bytes.')

# Read the key in hexadecimal digits from keyboard.
key_hex = raw_input('Type the key in ' + str(2*block) + ' hexadecimal digits: ')
key = binascii.unhexlify(key_hex)

# Decrypt the ciphertext.
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
ctx = cipher.decryptor()
padded_plaintext = ctx.update(ciphertext) + ctx.finalize()

# Unpad the plaintext.
ctx = padding.PKCS7(8*block).unpadder()
plaintext = ctx.update(padded_plaintext) + ctx.finalize()

# Write the decrypted text in the output file.
with open(filename + '.dec', 'wb') as f:
    f.write(plaintext)
print('Decrypted file: ' + filename + '.dec')
