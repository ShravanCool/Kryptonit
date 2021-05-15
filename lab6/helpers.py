from Crypto.Hash import SHA1
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64

# h = SHA1.new()
# h.update(b'Hello')
# print(h.hexdigest())

def get_hash(message):
    h = SHA1.new()
    message_bytes = message.encode()
    h.update(message_bytes)
    return h.hexdigest()

def rsakeys():
    length = 1024
    privatekey = RSA.generate(length, Random.new().read)
    publickey = privatekey.publickey()
    return privatekey, publickey

def encrypt(rsa_publickey, plain_text):
    # data = plain_text.encode()
    cipher = PKCS1_OAEP.new(rsa_publickey)
    ciphertext = cipher.encrypt(plain_text)
    return ciphertext

def decrypt(rsa_privatekey, ciphertext):
    cipher = PKCS1_OAEP.new(rsa_privatekey)
    message = cipher.decrypt(ciphertext)
    return message

def sign(privatekey, data):
    h = SHA1.new(data.encode())
    sign = pkcs1_15.new(privatekey).sign(h)
    return sign

def verify(publickey, data, sign):
    h = SHA1.new(data.encode())
    try:
        pkcs1_15.new(publickey).verify(h, sign)
        return True
    except:
        return False

def aeskey():
    return get_random_bytes(32)

def aesencrypt(message, key):
    if type(message) == str:
        data = message.encode()
    else:
        data = message
    cipher_encrypt = AES.new(key, AES.MODE_CFB)
    ciphered_bytes = cipher_encrypt.encrypt(data)
    iv = cipher_encrypt.iv
    return ciphered_bytes, iv

def aesdecrypt(cipher, key, iv):
    cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
    deciphered_bytes = cipher_decrypt.decrypt(cipher)
    return deciphered_bytes


