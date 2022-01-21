import socket
from common.common import recv_text, send, recv
from server.security.verification import verify_client
import settings
import threading

class server:

    ALL_CLIENTS = []
    ACCEPT_CLIENTS_THREAD = None

    def create_socket(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip, port))
        sock.listen(5)  # become a server socket, maximum 5 connections
        return sock

    def accept_client(self, sock):
        client, address = sock.accept()
        return client, address

    def keep_accepting(self, sock):
        while True:
            client, address = self.accept_client(sock)
            send(client, "hello")
            print(recv_text(client))
            if verify_client(client):
                self.ALL_CLIENTS.append([client, address])

    def __init__(self):
        sock = self.create_socket("0.0.0.0", settings.SOCKET.port)
        self.ACCEPT_CLIENTS_THREAD = threading.Thread(target=self.keep_accepting, args=[sock])
        self.ACCEPT_CLIENTS_THREAD.start()
        
