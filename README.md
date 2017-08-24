This script uses base libraries in Python 2.7.x to:

- download a remote webpage or
- read a local file
- find CVE numbers in either source
- remove any duplicate CVE numbers

Run it on any system with python installed by downloading the script and:

`python regex_pull_cve_numbers.py --file filename.txt`

or

`python regex_pull_cve_numbers.py --url http://example.com/some_security_bulletin`

View the help by

`python regex_pull_cve_numbers.py -h`

It will output the number of CVEs and all CVEs present.