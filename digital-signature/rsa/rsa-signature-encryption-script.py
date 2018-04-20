'''


DA CORREGGERE

https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
'''


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Cipher block size, expressed in bytes.
block = algorithms.AES.block_size/8

# Read the private key
with open('rsa_prvkey.pem', 'rb') as pk:
    pemtext = pk.read()
    print('Reading pem key.. ', pemtext)
    privateKey = serialization.load_pem_private_key(pemtext, None, default_backend())

# Read the public key for encryption
with open('rsa_pubkey.pem', 'rb') as pbk:
    pemtext = pbk.read()
    publicKey = serialization.load_pem_public_key(pemtext, default_backend())

# Read the plaintext file.
filename = raw_input('Type the file to sign: ')
with open(filename, 'rb') as f:
    plaintext = f.read()

signature = privateKey.sign(plaintext,
                            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                            salt_length=padding.PSS.MAX_LENGTH
                            ),
                        hashes.SHA256(),
                        )

# Write the encrypted file
iv = os.urandom(16)
salt = os.urandom(16)
key = raw_input("Insert key: ")
ps = PBKDF2HMAC(hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
keydigest = ps.derive(key)

# Pad the plaintext to make it multiple of the block size.
ctx = padding.PKCS7(8*block).padder()
padded_plaintext = ctx.update(plaintext) + ctx.finalize()

cipher = Cipher(algorithms.AES(keydigest), modes.CBC(iv), default_backend())
ctx = cipher.encryptor()
last_line = ''

with open(filename + '_encrypted', 'wb') as f:
    for line in padded_plaintext:
        cyphertext_line = ctx.update(line)
        f.write(cyphertext_line)
        last_line = line
    last_line = ctx.finalize()
    f.write(last_line)
    print('Encrypt-then-Signed file: ' + filename + '.enc')

last_line = ''
# Write the encrypted signature file
with open(filename + '.sgn', 'wb') as f:
    ctx = cipher.encryptor()
    ctx.update(signature)
    last_line = ctx.finalize()
    f.write(last_line)
    print('Encrypt-then-Signed file: ' + filename + '.enc' + '.sgn')
