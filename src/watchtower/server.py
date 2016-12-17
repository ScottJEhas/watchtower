import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
s.bind(('127.0.0.1', '5559'))

s.listen(5)
while True:
   c, addr = s.accept()
   print c.recv(1024)
   c.close()
