import random
from math import pow


def mod_exp(a, x, m):
    res = 1

    while x > 0:
        if x %2 == 0:
            res = (res*a) % m
        a = (a * a) % m
        x = x // 2

    return res % m

def main():
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)

    Xa = random.randint(2,q)
    Xm1 = random.randint(2,q)
    Xm2 = random.randint(2,q)
    Xb = random.randint(2,q)

    print("Secret key of user A:", Xa)
    print("Secret key of user B:", Xb)
    print("Secret key-1 of attacker M:", Xm1)
    print("Secret key-2 of attacker M:", Xm2)

    A = mod_exp(g, Xa, q)
    M1 = mod_exp(g, Xm1, q)
    M2 = mod_exp(g, Xm2, q)
    B = mod_exp(g, Xb, q)

    print("Public key intended to reach user B from user A intercepted by attacker M:", A)
    print("Public key intended to reach user A from user B intercepted by attacker M:", B)
    print("Public key generated by attacker M to send to user A:", M1)
    print("Public key generated by attacker M to send to user B:", M2)

    Sa = mod_exp(M1, Xa, q)
    Sm1 = mod_exp(A, Xm1, q)
    Sm2 = mod_exp(B, Xm2, q)
    Sb = mod_exp(M2, Xb, q)

    print("Secret key generated by user A due to interception by attacker M:", Sa)
    print("Secret key generated by user B due to interception by attacker M:", Sb)
    print("Actual secret key to be generated by user A:", Sm1)
    print("Actual secret key to be generated by user B:", Sm2)

main()
