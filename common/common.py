from common.security.encryption import decrypt, encrypt

def send(sock, text):
    send_bytes(sock, encrypt(text))
   
def send_bytes(sock, bytes):
    sock.send(bytes)

def recv(sock, buffer):
    recieved = sock.recv(buffer)
    total = b''
    while recieved != b'':
        total = total + recieved
        recieved = sock.recv(buffer)
    return total

def recv_text(sock, buffer=1024):
    recieved = sock.recv(buffer)
    return decrypt(recieved)

def decode(data):
    data = decrypt(data)
    return data