import socket
import threading
import time
import os

os.system("cls")
from pyfiglet import Figlet
os.system("color 3")
f = Figlet(font='puffy')
a = f.renderText("UDP CHAT APP")

print(a)

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

s.bind( ( "<Enter_Your_System_IP>",1234 ) )                                   #Bind  socket  
receiver_ip = input("Enter Your Friend IP address:")    


print("""
You are connected with your friend.
Start conversation.""")
	

def send():
	while True:
		os.system("color 3")
		msg = input("")
		s.sendto( msg.encode(),(receiver_ip,1234))
		time.sleep(0.2)

def receive():
	while True:
		os.system("color 2")
		data = s.recvfrom(2048)
		print ("\n\t\t\t\t\t-->" + "{}:".format(receiver_ip) + data[0].decode()) 
		time.sleep(0.1)
sender_thread = threading.Thread(target = send)
receiver_thread = threading.Thread(target = receive)

sender_thread.start()
receiver_thread.start()

