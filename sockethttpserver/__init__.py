import socket
import threading

HTTP_OK = "HTTP/1.0 200 OK\n\n"
HTTP_NOT_FOUND = "HTTP/1.0 404 NOT FOUND\n\n"

class httpserver():
    def __init__(self, host, port, loop):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.loop = loop

    def start(self):
        self.server.listen(1)
        def loop_function():
            while True:
                connection, address = self.server.accept()
                request = connection.recv(1024).decode()
                self.loop(request, connection, address)

        thread = threading.Thread(target=loop_function)
        thread.start()