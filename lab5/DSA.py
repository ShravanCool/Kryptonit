from SHA1 import SHA1HASH
from gmpy2 import xmpz, invert, powmod, is_prime
from random import randrange

class DSA:
    def __init__(self, L, N):
        self.L = L
        self.N = N

    def get_hash(self, message):

        hash_input = bytes(message, "utf-8")
        hash_digest = SHA1HASH(hash_input).final_hash()

        return hash_digest
        
    def generate_p_q(self):
        g = self.N
        n = (self.L-1) // g
        b = (L-1) % g

        while True:

            while True:
                s = xmpz(randrange(1, 2**(g)))
                a = self.get_hash(s)
                zz = xmpz((s+1) % (2 ** g))
                z = self.get_hash(zz)
                U = int(a,16) ^ int(z, 16)
                mask = 2 ** (N-1) + 1
                q = U | mask
                if is_prime(q,20):
                    break

            i,j = 0,2
            while i < 4096:
                V = []
                for k in range(n + 1):
                    arg = xmpz((s + j + k) % (2 ** g))
                    zzv = self.get_hash(arg)
                    V.append(int(zzv,16))
                W = 0
                for qq in range(n):
                    W += V[qq] * 2 ** (160 * qq)
                W += (V[n] % 2 ** b) * 2 ** (160 * n)
                X = W + 2 ** (L-1)
                c = X % (2 * q)
                p = X - c + 1
                if p >= 2 ** (L-1):
                    if is_prime(p, 10):
                        return p, q
                i += 1
                j += n + 1

    def generate_g(self, p, q):
        while True:
            h = randrange(2, p - 1)
            exp = xmpz((p - 1) // q)
            g = powmod(h, exp, p)
            if g > 1:
                break
        return g

    def generate_keys(self, g, p, q):

        x = randrange(2, q)
        y = powmod(g, x, p)

        return x, y

    def generate_params(self):
        p, q = generate_p_q(self.L, self.N)
        g = generate_g(p, q)
        return p, q, g

    def sign_document(self, input_file, p, q, g, x):

        if not validate_params(p, q, g):
            raise Exception("Invalid params")

        with open(input_file) as f:
            message = f.read()

        while True:
            k = randrange(2, q)
            r = powmod(g, k, p) % q
            m = self.get_hash(message)

            try:
                s = (invert(k, q) * (m + x * r)) % q
                return r, s
            except ZeroDivisionError:
                pass

    def verify(self, M, r, s, p, q, g, y):

        if not validate_params(p, q, g):
            raise Exception("Invalid params")

        if not validate_sign(r, s, q):
            return False

        try:
            w = invert(s, q)
        except ZeroDivisionError:
            return False

        m = self.get_hash(M)
        u1 = (m * w) % q
        u2 = (r * w) % q

        v = (powmod(g, u1, p) * powmod(y, u2, p)) % p % q

        if v == r:
            return True
        return False

    def validate_params(self, p, q, g):

        if is_prime(p) and is_prime(q):
            return True
        if powmod(g, q, p) == 1 and g > 1 and (p - 1) % q:
            return True
        return False

    def validate_sign(self, r, s, q):
        if r < 0 and r > q:
            return False
        if s < 0 and s > q:
            return False
        return True

def main():
    
    N, L = 160, 1024
    signer = DSA(L, N)

    p, q, g = signer.generate_params()
    print('P is {}, Q is {} and G is {}'.format(p,q,g))
    x, y = signer.generate_keys(g, p, q)
    print('Private key- {}'.format(x))
    print('Public key- {}'.format(y))

    input_file = './message.txt'
    r, s = signer.sign_document(input_file, p, q, g, x)
    print('Signature is r-{} and s-{}'.format(r, s))

    if signer.verify(input_file, r, s, p, q, g, y):
        print('All ok!!')
    else:
        print('Corrupted message!!')



main()
