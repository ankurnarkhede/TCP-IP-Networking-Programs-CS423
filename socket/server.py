import socket, threading
import sys

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress=clientAddress
        print("New connection added: ", clientAddress)

    def run(self):
        # error...after client exits, server keeps printing blank msgs
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == 'bye':
                break
            print("Client({}): ".format(self.clientAddress), msg)

            # print("Enter message to {}:".format(self.clientAddress),end='')
            print("Enter message to {}:".format(self.clientAddress))
            out_msg=sys.stdin.readline().strip()
            self.csocket.sendall(bytes(out_msg, 'UTF-8'))
        print("Client at ", self.clientAddress, " disconnected...")


def main():
    LOCALHOST = "127.0.0.1"
    PORT = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Server started")
    print("Waiting for client requests...")
    while True:
        server.listen(5)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock)
        newthread.start()

if __name__ == '__main__':
    main()