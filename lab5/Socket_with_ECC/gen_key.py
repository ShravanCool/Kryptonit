from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

privKey = generate_eth_key()
privKeyHex = privKey.to_hex()
pubKeyHex = privKey.public_key.to_hex()

print("Encryption public key:", pubKeyHex)
print("Decryption private key:", privKeyHex)

