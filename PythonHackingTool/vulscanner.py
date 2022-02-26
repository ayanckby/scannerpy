
import nmap3
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


nmap = nmap3.Nmap()
ip= input("Enter The Target ip: ")
version(ip, nmap)