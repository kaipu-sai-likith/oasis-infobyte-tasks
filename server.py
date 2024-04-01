import socket
import threading

def handle_client(client_socket, address):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            print(f"Connection with {address} closed.")
            break
        print(f"Received message from {address}: {message}")

def main():
    server_host = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, server_port))
    server_socket.listen(5)

    print(f"Server started on {server_host}:{server_port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection established with {address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    main()
