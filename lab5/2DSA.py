from SHA1 import SHA1HASH
from RSA import RSA

class DSA:

    def __init__(self, P, Q):
        self.P = P
        self.Q = Q
        self.encryptor = RSA(self.P, self.Q)
        self.e, self.d, self.n = self.encryptor.generate_keys()

    def get_hash(self, message):

        hash_input = bytes(message, "utf-8")
        hash_digest = SHA1HASH(hash_input).final_hash()

        return hash_digest

    def sign_document(self, input_file):

        with open(input_file) as f:
            message = f.read()

        hash_digest = self.get_hash(message)

        print("Public keys are e:{}, n:{}".format(self.e, self.n))
        print("Private keys are d:{}, n:{}".format(self.d, self.n))

        ciphertext = self.encryptor.encrypt(hash_digest)
        return ciphertext

    def verify_document(self, input_file, ciphertext):

        with open(input_file) as f:
            message = f.read()

        hash_digest = self.get_hash(message)

        plaintext = self.encryptor.decrypt(ciphertext)

        if plaintext == hash_digest:
            return False
        else:
            return True

def main():
    P, Q = 11, 13
    signer = DSA(11, 13)

    input_file = './message.txt'
    corrupted_file = './corrupted_message.txt'

    signature = signer.sign_document(input_file)
    print('Signature is-', signature)

    is_corrupted = signer.verify_document(corrupted_file, signature)

    if is_corrupted:
        print('Message has been corrupted!!')
    else:
        print('Message and signature verified successfully!!')

main()









