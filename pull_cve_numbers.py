import requests

def get_page(url):
	page = requests.get(url)
	return page.text

def get_cves(page):
    start_cve = page.find('CVE')
    if start_cve == -1: 
        return None, 0
    end_cve = start_cve + 14
    cve = page[start_cve:end_cve]
    return cve, end_cve

def prettyprint(cves):
	fixed_cves = []
	for cve in cves:
		if cve.find(":") != -1:
			cve = cve.replace(":","")
			print cve
			fixed_cves.append(cve)
		elif cve.find("<") != -1:
			cve = cve.replace("<","")
			print cve
			fixed_cves.append(cve)
	print "total: {}".format(len(cves)-1)
	print fixed_cves

def process():
	url = raw_input("Input a URL: ")
	page = get_page(url)
	cves = []
	while True:
		cve, end_position = get_cves(page)
		if cve:
			cves.append(cve)
			page = page[end_position:]
		else:
			break	
	prettyprint(cves)
	return cves

print process()