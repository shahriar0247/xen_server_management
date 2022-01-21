import socket
from common.common import send, recv

def connect_to_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    return server

server = connect_to_server("localhost",4000)
print(recv(server, 10))