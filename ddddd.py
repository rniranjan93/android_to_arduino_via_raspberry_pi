import socket
from serial import Serial
a = Serial('com13', 57600)
s = socket.socket()
port = 8080
s.bind(('192.168.43.181', port))
s.listen(1)
c, addr = s.accept()
print(addr)
print(c)
k = 0

while True:
	k = k+1
	throttle=c.recv(4).decode('utf')
	yaw = c.recv(4).decode('utf')
	pitch = c.recv(4).decode('utf')
	roll = c.recv(4).decode('utf')
	if k < 5:
		pitch = 1001
		roll = 1002
	print(pitch + " " + roll + " " + throttle + " " + yaw)
	a.write(pitch.encode('ascii'))
	a.write(roll.encode('ascii'))
	a.write(throttle.encode('ascii'))
	a.write(yaw.encode('ascii'))