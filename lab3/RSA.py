import random

def gcd(a,b):

    if b == 0:
        return a
    else:
        return gcd(b,a % b);

def mod_inverse(a, m):

    for x in range(1,m):
        if ((a%m) * (x%m)) % m == 1:
            return x

    return -1

class RSA:

    def __init__(self, P, Q):

        self.P = P
        self.Q = Q

        self.N = 0
        self.totient = 0

        self.E = 0
        self.D = 0

    def chooseE(self):
        
        while True:
            e = random.randint(2,self.totient)
            if gcd(e,self.N) == 1:
                return e

    def generate_keys(self):

        self.N = self.P * self.Q
        self.totient = (self.P-1) * (self.Q-1)

        self.E = self.chooseE()
        self.D = mod_inverse(self.E, self.N) 

        return self.E, self.D, self.N

    def encrypt(self, plaintext):

        cipher = [str((ord(plaintext[i]) * self.E) % self.N) for i in range(len(plaintext))]

        ciphertext = ' '.join(cipher)

        return ciphertext

    def decrypt(self, ciphertext):

        msg = []
        temp = 0
        for i in ciphertext:
            if i != ' ':
                temp*=10
                temp+=int(i)
            else:
                msg.append(temp)
                temp = 0

        msg.append(temp)

        for i in range(len(msg)):
            msg[i] = chr((msg[i] * self.D) % self.N)
            
        plaintext = ''.join(msg) 

        return plaintext

def main():
    P,Q = 11,13
    encryptor = RSA(P, Q)

    print("Prime numbers P and Q are {} and {}".format(P, Q))
    print("Generating the keys...")

    e, d, n = encryptor.generate_keys()

    print("Public keys are e:{}, n:{}".format(e, n))
    print("Private keys are d:{}, n:{}".format(d, n))

    message = "HelloWorld"
    print("Plain text: {}".format(message))

    ciphertext = encryptor.encrypt(message)
    print("Encrypted Text: {}".format(ciphertext))

    plaintext = encryptor.decrypt(ciphertext)
    print("Decrypted Text: {}".format(plaintext))

main()

