from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.36",9000)) 
data = s.recvfrom(10000)
print(data)
s.close()
