from server.output.output import send_all_data
from server.socket.init import server

def main():
    app = server()
    send_all_data(app.ALL_CLIENTS)