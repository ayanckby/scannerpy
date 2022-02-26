#!/usr/bin/python3

import socket
from datetime import datetime

t1= datetime.now()
def basicScanner() :
	s=socket.socket()
	s.settimeout(3)
	host=input("[+]Enter the ip: ")
	print ()
	print ("-"*80)
	print ("                Please Wait , Scanning is on going --------------->", host)
	print ("-"*80)
	for port in range (1,1001):
		if s.connect_ex((host,port)):
			pass
		else:
			print (f"{port} is open")

basicScanner()
t2=datetime.now()
t3=t2-t1
print (f"Time taken for Scanning {t3} Seconds")
