import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.150.143', 7004))

print('Bind UDP on 7004')

while True:
	data, addr = s.recvfrom(1024)
	print('Received from %s:%s.' % (addr, data))

s.close()