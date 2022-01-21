import socket
from common.common import recv_text, send, recv

def connect_to_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))
    return server

def main():
    server = connect_to_server("localhost",4000)
    send(server,"hello")
    print(recv_text(server))
    send(server,"hello")

