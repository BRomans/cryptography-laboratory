


from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import utils

# Read the public key
with open('ec_pubkey.pem', 'rb') as pbk:
    pemtext = pbk.read()
    publicKey = serialization.load_pem_public_key(pemtext, default_backend())

# Read the plaintext file.
filename = raw_input('Type the file to verify: ')
with open(filename, 'rb') as f:
    plaintext = f.read()

with open(filename + '.sgn', 'rb') as f:
    signature = f.read()
chosen_hash = hashes.SHA256()
hasher = hashes.Hash(chosen_hash, default_backend())
hasher.update(plaintext)
digest = hasher.finalize()
verification = publicKey.verify(signature,
                                digest,
                                ec.ECDSA(utils.Prehashed(chosen_hash))
                                )

print('Verification: ', verification)
print('Verified file: ' + filename + '.sgn')
