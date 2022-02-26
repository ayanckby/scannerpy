#!/usr/bin/python3
import socket
from datetime import datetime
import threading
from queue import Queue

t1= datetime.now()

#print_lock = threading.Lock()

#def threader():
#    while True:
#       worker = q.get()
#        scan(worker)
#       q.task_done()

#q = Queue()
def basicScanner() :
        s=socket.socket()
        #s.settimeout(3)
        host=input("[+]Enter the ip: ")
        host=socket.gethostbyname(host)
        print ()
        print ("-"*80)
        print ("                Please Wait , Scanning is on going --------------->", host)
        print ("-"*80)
        for port in range (1,1001):
            if s.connect_ex((host,port)):
                print (f"[-]port no {port} is clossed")
            else:
                print (f"[+++++]{port} is open") 

basicScanner()
t2=datetime.now()
t3=t2-t1
print (f"Time taken for Scanning {t3} Seconds")
