from socket import *
bufsize = 1024 # Modify to suit your needs
targetHost = "192.168.1.36"
listenPort = 1123

def forward(data, port):
    print("Forwarding: '%s' from port %s"% (data, port))
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("localhost", port))
    sock.sendto(data.encode(), (targetHost, listenPort))

def listen(host, port):
    listenSocket = socket(AF_INET, SOCK_DGRAM)
    listenSocket.bind((host, port))
    while True:
        data, addr = listenSocket.recvfrom(bufsize)
        forward(data, addr[1])

forward('hi',1123)
listen("localhost", listenPort)
