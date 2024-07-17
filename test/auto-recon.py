import os
# Install the required tools using pip
os.system("pip install subfinder")
os.system("pip install dirsearch")
os.system("pip install nmap")
os.system("pip install vulners")
os.system("pip install GetJS")
os.system("pip install GoLinkFinder")
os.system("pip install getallurls")
os.system("pip install WayBackUrls")
os.system("pip install WayBackRobots")
os.system("pip install MassDNS")
os.system("pip install Sublist3r")
os.system("pip install FFuF")
os.system("pip install XSSHunter")
os.system("pip install SQLMap")
os.system("pip install XXEInjector")
os.system("pip install SSRFDetector")
os.system("pip install GitTools")
os.system("pip install gitallsecrets")
os.system("pip install RaceTheWeb")
os.system("pip install CORStest")
os.system("pip install EyeWitness")
os.system("pip install parameth")
# Define the target domain
target_domain = "example.com"
# Use subfinder to find subdomains
os.system("subfinder -d " + target_domain + " -o subdomains.txt")
# Use dirsearch to search for directories
os.system("dirsearch -u " + target_domain + " -x 403,404 -t 20 -w wordlists/common.txt")
# Use nmap to scan for open ports
os.system("nmap -sS -sV -Pn -oA nmap_scan " + target_domain)
# Use vulners to check for vulnerabilities
os.system("vulners -s " + target_domain)