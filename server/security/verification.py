def verify_client(client):
    if client.recv() == "hello":
        return True