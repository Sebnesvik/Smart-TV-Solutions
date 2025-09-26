import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_socket(sock, host, port):
    sock.bind((host, port))

def listen_for_connections(sock):
    sock.listen()
    print("Server is listening for connections...")

def accept_connection(sock):
    conn, addr = sock.accept()
    print(f"Connection accepted from {addr}")
    return conn, addr

def handle_client(conn):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    except Exception as e:
        print(f"An error occurred: {e}")

def close_socket(sock):
    sock.close()
    print("Socket closed")

def main():
    host = "0.0.0.0"
    port = 5000
    server_socket = create_socket()
    try:
        bind_socket(server_socket, host, port)
        listen_for_connections(server_socket)
        conn, addr = accept_connection(server_socket)
        handle_client(conn)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        close_socket(server_socket)

if __name__ == "__main__":
    main()