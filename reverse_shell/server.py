import socket
import sys


def create_socket():
    try:
        return socket.socket()
    except socket.error as e:
        print(f"Socket creation error: {e}")


def bind_socket(sock, host, port):
    try:
        sock.bind((host, port))
        sock.listen(5)
    except socket.error as e:
        print(f"Cannot bind {host}:{port}. Error: {e}")
        bind_socket(sock, host, port)


def accept_socket(sock):
    connection, address = sock.accept()
    ip, port = address
    print(f"Connection established. | IP - {ip} | Port - {port}")

    send_command(connection, sock)
    connection.close()


def send_command(connection, socket):
    while True:
        command = input()
        if command == "quit":
            connection.close()
            socket.close()
            sys.exit()

        encoded_command = str.encode(command)
        if encoded_command:
            connection.send(encoded_command)
            client_response = str(connection.recv(1024), "utf-8")
            print(f"Client response: \n{client_response}")


def main():
    host = "192.168.0.107"
    port = 9997
    socket = create_socket()
    bind_socket(socket, host, port)
    accept_socket(socket)


main()
