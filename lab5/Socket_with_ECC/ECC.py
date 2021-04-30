from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
import binascii

# privKey = generate_eth_key()
# privKeyHex = privKey.to_hex()
# pubKeyHex = privKey.public_key.to_hex()

# print("Encryption public key:", pubKeyHex)
# print("Decryption private key:", privKeyHex)

# text = 'Hello World!!'
# plaintext = text.encode('UTF-8')
# print("Plaintext: ", plaintext)

# encrypted = encrypt(pubKeyHex, plaintext)
# print("Encrypted: ", binascii.hexlify(encrypted))

# decrypted = decrypt(privKeyHex, encrypted)
# msg = decrypted.decode('UTF-8')
# print("Decrypted: ", msg)

# userA_key = generate_eth_key()
# userB_key = generate_eth_key()

# userA_key = generate_key() 
# userB_key = generate_key()

# userA_privKeyHex = userA_key.to_hex()
# userA_pubKeyHex = userA_key.public_key.to_hex()

userA_privKeyHex = hex(0x1d779d5538505a53d364fd19ea46ea76b42e9f702ea4e545d8b46212de513205 )
userA_pubKeyHex = hex(0x8cc412524f5022fbb3b55ccee5546318daabd8a93effbb1e7ffe90ca9fd0730eca6e1d035e05fe520e123e749a6746f59afbb7b6fb903927541a06779378d43f)

# userA_privKeyHex = userA_key.secret
# userA_pubKeyHex = userA_key.public_key.format(True)

# userB_privKeyHex = userB_key.to_hex()
# userB_pubKeyHex = userB_key.public_key.to_hex()

userB_privKeyHex = hex(0x2496b535afd944a68c113d3199c5683fb0c474eb6ec73db3e967637577a09bbe )
userB_pubKeyHex = hex(0xdf0770602a28d74061a37c202e32b3a34a2342f2de1f277e455765e62d058137ace2a5d19b318ac650bebdc428a5fb9f541e2e2ebea530131db7fcb84cc66759)

def test():
    print(type(hex(userB_pubKeyHex)))
    print(type(hex(userB_privKeyHex)))

# userB_privKeyHex = userB_key.secret
# userB_pubKeyHex = userB_key.public_key.format(True)

def get_userA_keys():

    return userA_pubKeyHex, userA_privKeyHex


def get_userB_keys():

    return userB_pubKeyHex, userB_privKeyHex

def encrypt_A(text):
    message = text.encode('UTF-8')
    encrypted = encrypt(userA_pubKeyHex, message)
    return encrypted

def encrypt_B(text):
    message = text.encode('UTF-8')
    encrypted = encrypt(userB_pubKeyHex, message)
    return encrypted

def decrypt_A(cipher):
    decrypted = decrypt(userA_privKeyHex, cipher)
    plaintext = decrypted.decode('UTF-8')
    return plaintext

def decrypt_B(cipher):
    decrypted = decrypt(userB_privKeyHex, cipher)
    plaintext = decrypted.decode('UTF-8')
    return plaintext

def display_encrypted(cipher):
    return binascii.hexlify(cipher)

# test()
