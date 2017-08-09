import requests
import re

def get_page(url):
	page = requests.get(url)
	if page.text:
		print "[+] Page retrieved successfully"
		return page.text
	else:
		print "[-] Problem downloading page"
	
def remove_duplicates(cves):
	unique_cves = []
	for cve in cves:
		if cve not in unique_cves:
			unique_cves.append(cve)
	return unique_cves

def prettyprint(cves):
	print "[+] Listing unique CVEs"
	for cve in cves:
		print cve
	print "[+] Number of CVEs found: {}".format(str(len(cves)))
	return cves

def process():
	url = raw_input("Input a URL: ")
	page = get_page(url)
	cves = re.findall(r'CVE-\d{4}-\d{4,6}', page)
	if cves:
		cves = remove_duplicates(cves)
		prettyprint(cves)
	else:
		print "[-] No CVEs found"

process()