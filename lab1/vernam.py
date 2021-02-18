def encrypt(plain_text, key):
    length = len(key)
    cipher = ''
    for i in range(length):
        cipher += chr(ord(key[i])^ord(plain_text[i]))

    return cipher

def decrypt(cipher, key):
    length = len(key)
    plain_text = ''
    for i in range(length):
        plain_text += chr(ord(key[i])^ord(cipher[i]))

    return plain_text

def main():
    key = 'PLUTO'
    print("Key:", key)
    plain_text = 'HELLO'
    print("Message:", plain_text)
    cipher = encrypt(plain_text, key)
    # print(cipher)
    print("Encrypted Message:" + cipher)
    plain_text = decrypt(cipher, key)
    print("Decrypted Message:", plain_text)

main()

