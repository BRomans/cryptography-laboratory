'''
https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/
'''


from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

# Read the private key
with open('ec_prvkey.pem', 'rb') as pk:
    pemtext = pk.read()
    print('Reading pem key.. ', pemtext)
    privateKey = serialization.load_pem_private_key(pemtext, None, default_backend())


# Read the plaintext file.
filename = raw_input('Type the file to sign: ')
with open(filename, 'rb') as f:
    plaintext = f.read()
chosen_hash = hashes.SHA256()
hasher = hashes.Hash(chosen_hash, default_backend())
hasher.update(plaintext)
digest = hasher.finalize()

signature = privateKey.sign(digest,
                           ec.ECDSA(utils.Prehashed(chosen_hash))
                        )

# Write the signed file
with open(filename + '.sgn', 'wb') as f:
    f.write(signature)
print('Encrypt-then-Signed file: ' + filename + '.sgn')
