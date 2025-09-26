from smart_tv_server import SmartTV
tv = SmartTV()
import socket

def main():
    s = socket.socket()
    s.connect(("127.0.0.1", 1238))
    print("Connected to Smart TV. Type commands or 'exit' to quit. To see a list of commands write 'help'")

    commands = [
        "TURN_ON",
        "IS_ON",
        "GET_CHANNEL",
        "CHANNEL_UP",
        "CHANNEL_DOWN",
        "TURN_OFF",
    ]

    while True:
        cmd = input("Enter command: ").strip()
        if cmd.lower() == 'exit':
            break
        elif cmd.lower() == 'help':
            print("\nAvailable commands:")
            for c in commands:
                print(f"  - {c}")
            print("  - Exit")
            continue
        s.sendall(cmd.encode())
        response = s.recv(1024).decode()
        print("Response:", response)

    s.close()

if __name__ == "__main__":
    main()
