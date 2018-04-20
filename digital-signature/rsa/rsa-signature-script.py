'''

https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
'''



from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding



# Read the private key
with open('rsa_prvkey.pem', 'rb') as pk:
    pemtext = pk.read()
    print('Reading pem key.. ', pemtext)
    privateKey = serialization.load_pem_private_key(pemtext, None, default_backend())


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

# Write the signed file
with open(filename + '.sgn', 'wb') as f:
    f.write(signature)
print('Encrypt-then-Signed file: ' + filename + '.sgn')
