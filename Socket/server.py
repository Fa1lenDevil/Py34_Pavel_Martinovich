import socket
import requests


def server_script():
    host = socket.gethostname()
    port = 5050

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)

    conn, address = server_socket.accept()

    while True:
        url = conn.recv(1024).decode()
        data = requests.get(url)
        if data.status_code == 200:
            response = 'Successful'
            conn.send(response.encode())
            break
        if not data:
            break


if __name__ == "__main__":
    server_script()
