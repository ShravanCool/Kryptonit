from math import gcd
import sys
import hashlib
import math
import random

def loopIsPrime(number):
    isNumberPrime = True
    for i in range(20):
        isNumberPrime *= isPrime(number)
        if(isNumberPrime == False):
            return isNumberPrime
    return isNumberPrime

def modexp(base, exp, modulus ):
        return pow(base, exp, modulus)

def squareAndMultiply(x, c, n):
    z=1
    c="{0:b}".format(c)[::-1]
    l=len(c)
    for i in range(l-1, -1, -1):
        z=pow(z, 2)
        z=z%n
        if(c[i] == '1'):
            z=(z * x) % n
    return z

def keyGeneration():
    print("Computing key values, please wait...")
    loop = True
    while loop:
        k=random.randrange(2 ** (415), 2 ** (416))
        q=generateLargePrime(160)
        p=(k*q)+1
        while not (isPrime(p)):
            k=random.randrange(2 ** (415), 2 ** (416))
            q=generateLargePrime(160)
            p=(k * q)+1
        L = p.bit_length()

        t = random.randint(1, p-1)
        g = squareAndMultiply(t, (p-1) // q, p)

        if(L >= 512 and L <= 1024 and L % 64 == 0 and (gcd(p-1, q)) > 1 and squareAndMultiply(g, q, p) == 1):
            loop = False
            a = random.randint(2, q-1)
            h = squareAndMultiply(g, a, p)
            print("p = ", p)
            print("q = ", q)
            print("g = ", g)
            print("h = ", h)
            print("a = ", a)
    return (p, q, g, h, a)


def rabinMiller(num):

    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def isPrime(num):

    if (num < 2):
        return False

    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    return rabinMiller(num)

def generateLargePrime(keysize):
    while True:
        num = random.randrange(2 ** (keysize-1), 2 ** (keysize))
        if isPrime(num):
            return num

def computeInverse (in1, in2):
    aL = [in1]
    bL = [in2]
    tL = [0]
    t = 1
    sL = [1]
    s = 0
    q = math.floor((aL[0] / bL[0]))
    r = (aL[0] - (q * bL[0]))

    while r > 0 :
        temp = (tL[0] - (q * bL[0]))
        tL[0] = t
        t = temp
        temp = (sL[0] - (q * s))
        sL[0] = s
        s = temp
        aL[0] = bL[0]
        bL[0] = r
        q = math.floor(aL[0] / bL[0])
        r = (aL[0] - (q * bL[0]))

    r = bL[0]

    inverse = s % in2
    return inverse

def shaHash(fileName):
    BLOCKSIZE = 65536
    hasher = hashlib.sha1()
    with open(fileName, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    hex = "0x"+hasher.hexdigest()
    return int(hex,0) 

def sign(input_file, p, q, g, h, a):
    print(p)

    loop = True
    while loop:
        r = random.randint(1, q-1)
        c1 = squareAndMultiply(g, r, p)
        c1 = c1 % q
        c2 = shaHash(input_file) + (a * c1)
        Rinverse = computeInverse(r, q)
        c2 = (c2 * Rinverse) % q

        if(c1 != 0 and c2 != 0):
            loop = False
    print("c1  ", c1)
    print("c2  ", c2)
    return (c1, c2)

def verification(input_file, c1, c2, p, q, g, h):
    t1=shaHash(input_file)
    inverseC2 = computeInverse(c2, q)
    t1 = (t1 * inverseC2) % q

    t2 = computeInverse(c2, q)
    t2 = (t2 * c1) % q

    valid1 = squareAndMultiply(g, t1, p)
    valid2 = squareAndMultiply(h, t2, p)
    valid = ((valid1 * valid2) % p) % q
    if(valid == c1):
        print("Valid signature")
    else:
        print("Invalid signature")

def main():
    p, q, g, h, a = keyGeneration()

    input_file = './message.txt'
    c1, c2 = sign(input_file, p, q, g, h, a)

    verify_file = './corrupted_message.txt'
    # verify_file = './message.txt'
    verification(verify_file, c1, c2, p, q, g, h)

main()
