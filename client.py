import socket

# Create a socket
def create_client_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
def connect_to_server(socket, host, port):
    server_address = (host, port)
    socket.connect(server_address)

# Send data to the server
def send_data(socket, message):
    socket.sendall(message.encode())

# Receive data from the server
def receive_data(socket, buffer_size=4096):
    return socket.recv(buffer_size).decode()

def main():
    host = "0.0.0.0"
    port = 5000
    message = "Hello, server!"
    try:
        socket = create_client_socket()
        connect_to_server(socket, host, port)
        send_data(socket, message)
        response = receive_data(socket)
        print("Response from server:")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        socket.close()
        print("Connection closed")

if __name__ == "__main__":
    main()