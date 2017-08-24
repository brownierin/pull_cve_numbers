import requests
import re
import argparse

def get_page(url):
	try: 
		page = requests.get(url)
		print "[+] Page retrieved successfully"
		return page.text
	except:
		print "[-] Problem downloading page"

def get_file(filename):
	try:
		text = open(filename, "r")
		return text.read()
	except:
		print "[-] Problem opening file"

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
	if args.file:
		text = get_file(args.file)
	elif args.url:
		text = get_page(args.url)
	cves = re.findall(r'CVE-\d{4}-\d{4,6}', text)
	if cves:
		cves = remove_duplicates(cves)
		prettyprint(cves)
	else:
		print "[-] No CVEs found"
	
parser = argparse.ArgumentParser(description='Pulls CVEs from either a \
	page or from a file')
group = parser.add_mutually_exclusive_group()
group.add_argument('--url', '-u',
                help='the url of the page')
group.add_argument('--file', '-f', help="name of the file to process")
args = parser.parse_args()
print args

process()