import socket
print "This software scan ports from 0 to 100000 -- @omaryahir"
print ""
IPHOST = raw_input("Write IP or name of host: ")
PORT_S = raw_input("Start with port: ")
PORT_F = raw_input("Finish with port: ")
closed = ""
opened = ""

print "RESUME: "
for port_number in range(int(PORT_S),int(PORT_F)):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
	result = s.connect_ex((IPHOST,port_number))
	if(result==0):
		print "OPEN: " + str(port_number)		
	
	s.close()