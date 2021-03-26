import random
from math import pow

a = random.randint(2, 10)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gen_key(q):

    while True:
        key = random.randint(pow(10, 20), q)
        if gcd(q, key) == 1:
            return key

def mod_exp(a, x, m):
    res = 1

    while x > 0:
        if x % 2 == 0:
            res = (res*a) % m
        a = (a * a) % m
        x = x // 2

    return res % m

def encrypt(msg, q, h, g): 
  
    en_msg = [] 
  
    k = gen_key(q)# Private key for sender 
    s = mod_exp(h, k, q) 
    p = mod_exp(g, k, q) 
      
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
  
    # print("g^k used : ", p) 
    # print("g^ak used : ", s) 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i]) 
  
    return en_msg, p 
  
def decrypt(en_msg, p, key, q): 
  
    dr_msg = [] 
    h = mod_exp(p, key, q) 
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/h))) 
          
    return dr_msg 
  
# Driver code 
def main(): 
  
    msg = 'HelloWorld'
    print("Plain text:", msg) 
  
    q = random.randint(pow(10, 20), pow(10, 50)) 
    g = random.randint(2, q) 
  
    key = gen_key(q)# Private key for receiver 
    h = mod_exp(g, key, q) 
    # print("g used : ", g) 
    # print("g^a used : ", h) 

    print("Public keys are {},\n{},\nand {}".format(q, h, g))
  
    en_msg, p = encrypt(msg, q, h, g) 
    # print("Encrypted Message: {},\n and {}".format(en_msg, p))
    print("Encrypted Messages are- Message: ")
    for i in en_msg:
        print(i)
    print("and P:", p)
    dr_msg = decrypt(en_msg, p, key, q) 
    dmsg = ''.join(dr_msg) 
    print("Decrypted Message :", dmsg); 
  
  
main() 



