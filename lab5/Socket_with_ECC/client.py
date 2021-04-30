from ECC import get_userB_keys, encrypt_A, decrypt_B, display_encrypted
import socket

def client_program():

    pub_key, priv_key = get_userB_keys()
    print("Public key of user B: ", pub_key)
    print("Private key of user B: ", priv_key)

    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'end':

        message = encrypt_A(message)

        client_socket.send(message)
        data = client_socket.recv(1024)

        hex_text = display_encrypted(data)
        plaintext = decrypt_B(data)

        print('From connected userA: ', hex_text)
        print('Decrypted message from userA: ', plaintext)

        message = input(" -> ")

    client_socket.close()

def main():
    client_program()

main()
