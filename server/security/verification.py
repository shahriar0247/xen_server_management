from common.common import recv_text

def verify_client(client):
    if recv_text(client) == "hello":
        return True