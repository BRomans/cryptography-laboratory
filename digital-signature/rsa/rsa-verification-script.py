


from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding


with open('rsa_pubkey.pem', 'rb') as pbk:
    pemtext = pbk.read()
    publicKey = serialization.load_pem_public_key(pemtext, default_backend())

# Read the plaintext file.
filename = raw_input('Type the file to verify: ')
with open(filename, 'rb') as f:
    plaintext = f.read()

with open(filename + '.sgn', 'rb') as f:
    signature = f.read()

verification = publicKey.verify(signature,
                                plaintext,
                                padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                                salt_length=padding.PSS.MAX_LENGTH
                                ),
                                hashes.SHA256(),
                                )

print('Verification: ', verification)
print('Verified file: ' + filename + '.sgn')
