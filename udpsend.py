'''
OSC Reference: http://opensoundcontrol.org/book/export/html/1


OSC Packet : 2 tyes
	OSC Message: 
	OSC Address Pattern followed by an 
	OSC Type Tag String followed by zero or more OSC Arguments.

		OSC Address Patterns:  OSC-string beginning with the character '/' 

	OSC Bundle:
		Byte 1: '/'
		B


'''
import socket
host = "localhost"
port = 7400
#print(type(buf))
addr = (host, port)

OSC_ADDRESS = "/1/xyz\0\0"
OSC_TYPE_TAG = ",sss\0\0\0\0"
ARG1="2.2\0"
ARG2="1.0\0"
ARG3="3.33322\0"
encoded_message=(OSC_ADDRESS+OSC_TYPE_TAG+ARG1+ARG2+ARG3).encode()
UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
'''
buf=bytearray(len(encoded_message)+4)
i = 0
while i < len(encoded_message):
	buf[i]=encoded_message[i]
	i += 1
j=0
while i < len(buf):
	buf[i]=ARG4[j]
	i+=1
	j+=1

print(buf)
print(len(buf))
'''

UDPSock.sendto(encoded_message, (host, port))
'''
def_msg = "===Enter message to send to server===";
print(def_msg)
while (1):
	data = input('>> ')
	if not data:
		break
	else:
		if(UDPSock.sendto(data,addr)):
			print( "Sending message '",data,"'.....")
'''
# Close socket
UDPSock.close()
