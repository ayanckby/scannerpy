import re
import requests

def emailharvester():
	url=input("Enter The Full URL: \n=>")
	EMAIL_REGEX=r"[\w\.-]+[\w\.-]+"
	r=requests.get(url)
	for re_match in re.findall(EMAIL_REGEX, r.text):
		print(re_match)

emailharvester()