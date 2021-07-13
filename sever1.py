import socket
import con
s=socket.socket()
s.bind(("localhost",8989))
s.listen(4)
print("===================================")
print("sever side program is ready to accept")
print("====================================")
while(True):
	con.addr=s.accept()
	print("type of con=",type(con))
	print("type of addr=",type(addr))
	print("==================================")
	cdata=con.recv(1024).decode()
	print("Data form cilent at server side={}".format(cdata))
	print("==================================")
	con.send("Hi ,This is ajay form sever side".encode())
