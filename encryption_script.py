# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 12:53:17 2018

@author: Michele Romani

key: 51234567890987654567543245678903

ENCRYPTION SCRIPT
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.backends import default_backend
import numpy as np
import os

iv = os.urandom(16)
file_in  = open("plaintext.txt") 
file_out = open("output.enc", "w")

key = input("Insert key: ")

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend()) 
ctx = cipher.encryptor()
last_line = ""
for line in file_in:
    cyphertext_line = ctx.update(line)
    file_out.write(cyphertext_line)
    last_line = line
last_line = ctx.finalize()
file_out.write(last_line)