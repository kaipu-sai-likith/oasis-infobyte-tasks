import socket

def main():
    server_host = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_host, server_port))
        print("Connected to the server.")
        
        while True:
            message = input("Enter message (type 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            client_socket.send(message.encode())
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
