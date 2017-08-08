This script uses base libraries in Python 2.7.x to:

- download a remote webpage
- find CVE numbers in that webpage
- remove any duplicate CVE numbers

Run it on any system with python installed by downloading the file and:

python regex_pull_cve_numbers.py

Type in the URL of the security bulletin, and it will output the number of CVEs and all CVEs present.