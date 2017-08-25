import requests
import re
import argparse

def get_page(url):
    try: 
        page = requests.get(url)
        print "[+] Page retrieved successfully"
        return page.text
    except Exception:
        print "[-] Problem downloading page"

def get_file(filename):
    try:
        return open(filename, "r").read()
    except Exception:
        print "[-] Problem opening file"

def prettyprint(cves):
    print "[+] Listing unique CVEs"
    for cve in cves:
        print cve
    print "[+] Number of CVEs found: {}".format(len(cves))

def process():
    if args.file:
        text = get_file(args.file)
    elif args.url:
        text = get_page(args.url)
    cves = re.findall(r'CVE-\d{4}-\d{4,10}', text)
    if cves:
        prettyprint(set(cves))
    else:
        print "[-] No CVEs found"
    
parser = argparse.ArgumentParser(description='Pulls CVEs from either a \
    webpage or from a file')
group = parser.add_mutually_exclusive_group()
group.add_argument('--url', '-u', help='the url of the page')
group.add_argument('--file', '-f', help="name of the file to process")
args = parser.parse_args()

process()