import math

def mod_inverse(a, m):
    a %= m

    for x in range(-m,m):
        if (a*x) % m == 1:
            return x

def get_cofactor(A, temp, p, q, n):
    i,j = 0,0

    for row in range(n):
        for col in range(n):
            if row != p and col != q:
                temp[i][j] = A[row][col]
                j += 1
                if j == n-1:
                    j = 0
                    i += 1

def determinant(A, n, N):
    D = 0
    if n == 1:
        return A[0][0]
    
    temp = [[0]*N for i in range(N)]
    sign = 1

    for f in range(n):
        get_cofactor(A, temp, 0, f, n)
        D += sign * A[0][f] * determinant(temp, n-1, N)
        sign *= -1

    return D

def adjoint(A, adj, N):
    if N == 1:
        adj[0][0] = 1
        return

    sign = 1
    temp = [[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            get_cofactor(A, temp, i, j, N)
            sign = 1 if (i+j) % 2 == 0 else -1
            adj[j][i] = sign * determinant(temp, N-1, N)

def is_inverse(A, inv, N):
    det = determinant(A, N, N)
    if det == 0:
        print('Inverse of matric does not exist!!')
        return False

    inv_det = mod_inverse(det, 26)
    adj = [[0]*N for i in range(N)]
    adjoint(A, adj, N)
    for i in range(N):
        for j in range(N):
            inv[i][j] = (adj[i][j] * inv_det) % 26

    return True

def create_key_matrix(key, N):
    key_matrix = [[0]*N for i in range(N)]
    # N = int(intput('Enter the size of key matrix:'))
    # key_matrix = []
    # for i in range(N):
        # temp = list(map(int,intput().split()))
        # key_matrix.append(temp)

    k = 0
    for i in range(N):
        for j in range(N):
            key_matrix[i][j] = ord(key[k]) % 65
            k += 1

    return key_matrix

def mat_mul_encrypt(text_vector, key_matrix, N):
    cipher_vector = [ [0] for i in range(N)]

    for i in range(N):
        for j in range(N):
            cipher_vector[i][0] += (key_matrix[i][j]*text_vector[j][0])

        cipher_vector[i][0] %= 26

    return cipher_vector

def encrypt(plain_text, key):
    N = int(math.sqrt(len(key))) 
    key_matrix = create_key_matrix(key,N)
    # print(key_matrix)

    rem = N - len(plain_text)
    rem_str = 'X'*rem
    plain_text += rem_str

    text_vector = [[0] for i in range(N)]

    for i in range(N):
        text_vector[i][0] = ord(plain_text[i]) % 65

    # print(text_vector)

    cipher_vector = mat_mul_encrypt(text_vector, key_matrix, N)

    cipher_text = ''
    for i in range(N):
        cipher_text += chr(cipher_vector[i][0] + 65)

    return cipher_text

def decrypt(cipher, key):
    N = int(math.sqrt(len(key))) 
    key_matrix = create_key_matrix(key, N)

    inv = [[0]*N for i in range(N)]

    if is_inverse(key_matrix, inv, N):
        print('Inverse exists!!')

    print(inv)
    plain_text = ''
    k = 0
    while k < len(cipher):
        for i in range(N):
            sum = 0
            temp = k
            for j in range(N):
                sum += ((inv[i][j] + 26)%26 * (ord(cipher[temp])%26)) % 26
                sum %= 26
                temp += 1

            plain_text = chr(sum)

        k += N

    f = len(plain_text) - 1
    while plain_text[f] == 'x':
        f -= 1

    return plain_text[:f+1]

def main():
    plain_text = "ACT"
    print('Message:', plain_text)
    key = "GYBNQKURP"
    print('Key:', key)
    cipher = encrypt(plain_text, key)
    print('Encrypted message:', cipher)
    plain_text = decrypt(cipher, key)
    print('Decrypted message:', plain_text)

main()

