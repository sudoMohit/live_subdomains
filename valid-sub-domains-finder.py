import os
import requests
import argparse
import sys
import urllib3
def valid(file,domain_name):
    domain_list = []
    num = 1
    j = 0
    with open(file) as f:
        file_list = f.read().split('\n')
        for i in file_list:
            domain_list.append(i.split(domain_name)[0])
        for x in domain_list:
            domain_list[j] = x.lower()
            j += 1 
        sorted_domain_list = sorted(domain_list)
        for j in sorted_domain_list:
            try:
                url = requests.get(f'https://{j}{domain_name}',headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"},allow_redirects=False)
                code = url.status_code
            except requests.exceptions.ConnectionError:
                code = "connection refused"
            except requests.exceptions.InvalidURL:
                code = "invalid url"
            except requests.exceptions.ReadTimeout:
                code = "Can't read from server."
            except requests.exceptions.ChunkedEncodingError:
                code = "Chunked Encoding Error."
            except urllib3.exceptions.LocationParseError:
                code = "Invalid url"
            if(code == 200):
                with open(f"final sorted {domain_name} subdomains.txt", 'a') as g:
                    g.write(f"{j}{domain_name}\n")
            elif(code == 403 or code == 301 or code == 302 or code == 501 or code == 502 or code == 503 or code == 504 or code == 505):
                with open(f"403_final sorted {domain_name} subdomains.txt", 'a') as g:
                    g.write(f"{j}{domain_name}\n")
                    
            
            print(f"{num}: https://{j}{domain_name} : {code}")
            num += 1

valid("samsung.txt",".coca-colacompany.com")
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--file','-f',type=str, help='takes file that contains raw subdomains')
#     parser.add_argument('--domain','-d', type=str, help='takes a domain name e.g ".example.com"')
#     args = parser.parse_args()
#     sys.stdout.write(valid(args.file, args.domain))