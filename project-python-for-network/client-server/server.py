import socket
PORT = 10000
service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(("", PORT))
service.listen(1)
print "listening on port", PORT
while 1:
    channel, info = service.accept()
    print info
    channel.send("HELLO WORLD")
    channel.close()