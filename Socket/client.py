import socket


def client_script():
    host = socket.gethostname()
    port = 5050

    client_socket = socket.socket()
    client_socket.connect((host, port))

    url = input('Enter your website: ')

    while url.lower() != 'finish':
        client_socket.send(url.encode())
        response = client_socket.recv(1024).decode()
        print(f"Response is {response}")
    client_socket.close()


if __name__ == '__main__':
    client_script()