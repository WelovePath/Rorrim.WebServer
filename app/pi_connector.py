import socket
import threading
from app import Mirror


class pi_connector(threading.Thread):

    def __init__(self, host, port):
        self.mirror_list = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.wait_for_client(host, port)
        threading.Thread.__init__(self)

    def wait_for_client(self, host, port):
        self.server_socket.bind((host, port))
        self.server_socket.listen(10)

    def run(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            mirror = Mirror.Mirror(client_socket)
            self.mirror_list.append(mirror)
