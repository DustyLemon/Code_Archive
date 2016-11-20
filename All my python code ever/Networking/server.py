from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("192.168.1.36",9000))
s.listen(5)
while True:
    c,a = s.accept()
    print("Received connection from", a)
    message = input()
    c.send((message).encode())
    c.close()
