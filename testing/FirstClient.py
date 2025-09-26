import socket

def main():
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

    # Connecting to server
    try:
        s.connect(('ntnu.no', 80))
        print("Socket successfully connected")
    except Exception as e:
        print(f"Socket connection failed: {e}")
        s.close()
        return

    # Wait for user input to close the connection
    input("Press Enter to close the connection...")
    s.close()
    print("Connection closed")

if __name__ == "__main__":
    main()