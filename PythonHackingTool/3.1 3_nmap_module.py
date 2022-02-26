import nmap3
import time

def host_discovery(ip,nmap):
	results = nmap.nmap_no_portscan(ip)
	print("-"*50)
	print(ip)
	results = results['runtime']
	results = results['summary']
	results = results.split("ress (")
	results = results[1].split(' ho')
	results = results[0]
	if results == "1":
		print("Host up")
	else:
		print("Host down")

def os(ip,nmap):
	results = nmap.nmap_os_detection(ip)
	for i in results:
		print("-"*50)
		os = i['name']
		accuracy = i['accuracy']
		print("OS is "+os+" and accuracy is "+accuracy+"%")

def version(ip,nmap):
	results = nmap.nmap_version_detection(ip)
	print("-"*50)
	print(ip)
	for i in results:
		protocol = i['protocol']
		port = i['port']
		state = i['state']
		service = i['service']
		for j in service.keys():
			if "product" in j:
				product = service['product']
			else:
				pass
			if "name" in j:
				name = service['name']
			else:
				pass
			if "version" in j:
				version = service['version']
			else:
				pass

		print(f"Protocol => {protocol}")
		print(f"Port => {port}")
		print(f"State => {state}")
		print(f"Product => {product}")
		print(f"Name => {name}")
		print(f"Version => {version}")
		print("\n")

def top_ports(ip,nmap):
	top_port =  nmap.scan_top_ports(ip)
	print("-"*50)
	print(ip)
	for i in top_port[ip]:
		protocol = i['protocol']
		port = i['portid']
		state = i['state']
		service = i['service']
		for i in service.keys():
			if "name" in i:
				name = service['name']
			else:
				pass
		print(f"Protocol => {protocol}")
		print(f"Port => {port}")
		print(f"State => {state}")
		print(f"Service => {name}")

def syn_scan(ip):
	nmap = nmap3.NmapScanTechniques()
	nmap_syn_scan = nmap.nmap_syn_scan(ip)
	print("-"*50)
	print(ip)
	for i in nmap_syn_scan[ip]:
		protocol = i['protocol']
		port = i['portid']
		state = i['state']
		service = i['service']
		for i in service.keys():
			if "name" in i:
				name = service['name']
			else:
				pass
		print(f"Protocol => {protocol}")
		print(f"Port => {port}")
		print(f"State => {state}")
		print(f"Service => {name}")
		print("\n")

def switcher():
	modo = int(input("Choose mode\n[1]. OS Detection\n[2]. Version Detection\n[3]. Top Ports\n[4]. Syn Scan\n[#]. Exit\n=> "))
	ip = input("Whats your ip?\n=> ")
	nmap = nmap3.Nmap()
	if modo == 1:
		os(ip,nmap)
	elif modo == 2:
		version(ip,nmap)
	elif modo == 3:
		top_ports(ip,nmap)
	elif modo == 4:
		syn_scan(ip)
	else:
		time.sleep(1)
		print("Closing...")
		exit()

def main():
	print("Welcome NMAP with PYTHON")
	print("[1]. Scan\n[2]. Host Discovery\n[#]. Exit")
	modo = int(input("=> "))
	if modo == 1:
		switcher()
	elif modo == 2:
		ip = input("IP please=> ")
		nmap = nmap3.NmapHostDiscovery()
		host_discovery(ip,nmap)
	else:
		exit()

if __name__ == '__main__':
	try:
		main()
	except:
		exit()