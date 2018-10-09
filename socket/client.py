import socket
import sys

def main():
    SERVER = "127.0.0.1"
    PORT = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))

    client.sendall(bytes("Initial msg from client", 'UTF-8'))

    while True:
        in_data = client.recv(1024)
        print("Server:", in_data.decode())
        # print("Client: ",end='')
        print("Client: ")
        out_data = sys.stdin.readline().strip()

        client.sendall(bytes(out_data, 'UTF-8'))
        if out_data == 'bye':
            break

    client.close()
    sys.exit(0)

if __name__ == '__main__':
    main()