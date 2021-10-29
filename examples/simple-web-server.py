import sockethttpserver

HTTP_OK = "HTTP/1.0 200 OK\n\n"

def loop(request, connection, address):
    response = HTTP_OK+"Hello world"
    connection.sendall(response.encode())
    connection.close()


server = sockethttpserver.httpserver("localhost", 8000, loop)
server.start()