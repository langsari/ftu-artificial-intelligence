import socket
Host = "10.20.42.90"
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, port))
result = s.recv(1024)
s.close()
print result