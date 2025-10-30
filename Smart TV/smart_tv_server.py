import socket
import threading

class SmartTV:
    def __init__(self, num_channels=10):
        self.is_on = False
        self.current_channel = 1
        self.num_channels = num_channels

    def handle_command(self, cmd):
        parts = cmd.split()
        if not parts:
            return "UNKNOWN COMMAND"

        command = parts[0].upper()
        args = parts[1:]

        if not self.is_on and command not in ["TURN_ON", "IS_ON"]:
            return "TV is OFF. Please turn it ON first."

        if command == "TURN_ON":
            self.is_on = True
            return "TV is now ON"
        elif command == "TURN_OFF":
            self.is_on = False
            return "TV is now OFF"
        elif command == "IS_ON":
            return "ON" if self.is_on else "OFF"
        elif command == "GET_CHANNEL":
            return str(self.current_channel)
        elif command == "CHANNEL_UP":
            if self.current_channel < self.num_channels:
                self.current_channel += 1
            return str(self.current_channel)
        elif command == "CHANNEL_DOWN":
            if self.current_channel > 1:
                self.current_channel -= 1
            return str(self.current_channel)
        elif command == "SET_CHANNEL":
            if len(args) != 1 or not args[0].isdigit():
                return "ERROR: SET_CHANNEL requires a channel number"
            ch = int(args[0])
            if 1 <= ch <= self.num_channels:
                self.current_channel = ch
                return str(self.current_channel)
            else:
                return "ERROR: Channel out of range"
        else:
            return "UNKNOWN COMMAND"

def handle_client(conn, tv):
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            response = tv.handle_command(data)
            conn.sendall(response.encode())
    except Exception as e:
        print(f"An error occurred with a client {e}")
    finally:
        conn.close()


def main():
    tv = SmartTV()
    s = socket.socket()
    s.bind(("127.0.0.1", 1238))
    s.listen(5)
    print("TV server running and accepting multiple clients")

    try:
        while True:
            conn, addr = s.accept()
            print(f"Connected to client: {addr}")
            client_thread = threading.Thread(target=handle_client, args=(conn, tv))
            client_thread.daemon = True
            client_thread.start()
    except Exception as e:
        print(f"An error occurred in the server: {e}")
    finally:
        s.close()


if __name__ == "__main__":
    main()