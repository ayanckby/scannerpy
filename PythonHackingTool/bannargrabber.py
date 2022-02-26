#!/usr/bin/python3

import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s=socket.socket()
        s.connect((ip,port))
        banner=s.recv(1024)
        return banner
    except:
        return    

def bannergrabber():
    ip= input("Enter Your ip or Website you Want to Scan and Grab the banner:  ")
    port_lst =(input("Enter the required ports separating with a space( ):  "))
    ports = port_lst.split()
    print(ports)
    for port in ports:
        #port=80
        banner=retBanner(ip,int(port)).strip("b")
        if banner:
            
            print(f"[++] {ip} : port no : {port} : {banner}")


bannergrabber()
