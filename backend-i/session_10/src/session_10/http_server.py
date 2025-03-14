import socket
import logging 

# Define the host and port to listen on
HOST, PORT = '127.0.0.1', 8080

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    try:
        # Allow immediate reuse of address after program exit
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind the socket to the host and port
        server_socket.bind((HOST, PORT))
        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Serving HTTP on {HOST} port {PORT} ...")
    
    except Exception as e:
        logging.error("There was an error with socket: ", e)

    try:

        while True:
            # Accept a new client connection
            client_connection, client_address = server_socket.accept()
            with client_connection:
                # Receive the request data (limit to 1024 bytes for simplicity)
                request_data = client_connection.recv(1024).decode('utf-8')
                print("Received request:")
                print(request_data)

                first_line = request_data.splitlines()[0]
                method, path, _ = first_line.split(" ")

                # Print the HTTP method and requested path
                print(f"HTTP Method: {method}")
                print(f"Requested Path: {path}")


                # Construct a simple HTTP response
                if path == "/":
                    http_response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        "Content-Length: 46\r\n"
                        "\r\n"
                        "<html><body><h1>Estas na pagina principal</h1></body></html>"
                    )
                elif path == "/about":
                    http_response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        "Content-Length: 46\r\n"
                        "\r\n"
                        "<html><body><h1>About Us</h1></body></html>"
                    )
                else:
                    # If the path is not supported, return a 404 response
                    http_response = (
                        "HTTP/1.1 404 Not Found\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        "Content-Length: 58\r\n"
                        "\r\n"
                        "<html><body><h1>404 Not Found</h1><p>The page you requested does not exist.</p></body></html>"
                    )

                # Send the HTTP response back to the client
                client_connection.sendall(http_response.encode('utf-8'))
        
    except Exception as e:
        logging.error("There was an error with connection: ", e)