def create_key(keyword, length):
    key = ''
    for i in range(length):
        key += keyword[i%len(keyword)]

    return key

def encrypt(plain_text, keyword):
    key = create_key(keyword, len(plain_text))
    cipher = ''
    for i in range(len(plain_text)):
        x = (ord(plain_text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher += chr(x)

    return cipher

def decrypt(cipher, keyword):
    key = create_key(keyword, len(cipher))
    plain_text = ''
    for i in range(len(cipher)):
        x = (ord(cipher[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        plain_text += chr(x)
    
    return plain_text

def main():
    keyword = 'PLUTO'
    print("key:", keyword)
    plain_text = 'SCHIZOPHRENIA'
    print("Message:", plain_text)
    cipher = encrypt(plain_text, keyword)
    print("Encrypted Message:", cipher)
    plain_text = decrypt(cipher, keyword)
    print("Decrypted Message:", plain_text)

main()


