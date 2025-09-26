import socket

tv_on = False
current_channel = 1
total_channels = 10

def handle_command(cmd):
    global tv_on, current_channel
    cmd = cmd.strip().upper()

    if cmd == "TURN_ON":
        tv_on = True
        return "TV is now ON"
    elif cmd == "TURN_OFF":
        tv_on = False
        return "TV is now OFF"
    elif cmd == "IS_ON":
        return "ON" if tv_on else "OFF"
    elif not tv_on:
        return "TV is OFF. Please turn it ON first."
    elif cmd == "GET_CHANNEL":
        return str(current_channel)
    elif cmd == "CHANNEL_UP":
        if current_channel < total_channels:
            current_channel += 1
        return str(current_channel)
    elif cmd == "CHANNEL_DOWN":
        if current_channel > 1:
            current_channel -= 1
        return str(current_channel)
    else:
        return "UNKNOWN COMMAND"

def main():
    s = socket.socket()
    s.bind(("127.0.0.1", 1238))
    s.listen(1)
    print("TV server running")
    conn, addr = s.accept()
    print("Connected:", addr)
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        response = handle_command(data)
        conn.sendall(response.encode())
    conn.close()
    s.close()

if __name__ == "__main__":
    main()