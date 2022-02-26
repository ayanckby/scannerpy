import nmap3
from nmap3.nmap3 import Nmap

def version(ip, nmap):
	results = nmap.nmap_version_detection(ip)
	print("-"*50)
	print(results)
	for i,j in results:
		if i in results:
			print(f"{results[i]}::::{results[j]}")
		





nmap = nmap3.Nmap()
ip= input("Enter The Target ip: ")
version(ip, nmap)