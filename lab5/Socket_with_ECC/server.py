# User A
from ECC import get_userA_keys, encrypt_B, decrypt_A, display_encrypted
import socket

def server_program():

    pub_key, priv_key = get_userA_keys()
    print("Public key of user A: ", pub_key)
    print("Private key of user A: ", priv_key)

    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, addrs = server_socket.accept()
    print("Connection from userB: ", str(addrs))

    while True:

        data = conn.recv(1024)
        if not data:
            break

        hex_text = display_encrypted(data)
        message = decrypt_A(data)

        print("From connected userB: ", hex_text)
        print("Decrypted message from userB: ", message)
        data = input(' -> ')
        cipher = encrypt_B(data)
        conn.send(cipher)

    conn.close()

def main():
    server_program()

main()
