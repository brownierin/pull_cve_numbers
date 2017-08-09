import re
	
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
	filename = raw_input("Input the filename: ")
	text = open(filename, "r")
	cves = re.findall(r'CVE-\d{4}-\d{4,6}', text.read())
	if cves:
		cves = remove_duplicates(cves)
		prettyprint(cves)
	else:
		print "[-] No CVEs found"

process()