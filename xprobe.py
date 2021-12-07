from colorama import Fore
from fake_useragent import UserAgent
import requests
import concurrent.futures
import argparse
import socket
import subprocess

banner = """


██   ██       ██████  ██████   ██████  ██████  ███████ 
 ██ ██        ██   ██ ██   ██ ██    ██ ██   ██ ██      
  ███   █████ ██████  ██████  ██    ██ ██████  █████   
 ██ ██        ██      ██   ██ ██    ██ ██   ██ ██      
██   ██       ██      ██   ██  ██████  ██████  ███████ 
                                                       v1.0

by c0d3ninja
"""


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.add_argument('-url', '--urls',
                    type=str, help='Domains to probe')

group.add_argument('-sc', '--statuscode', action='store_true',
                    help='HTTP Status Codes')

group.add_argument('-p', '--preferhttps', action='store_true',
                    help='Display https only domains')

group.add_argument('-sr', '--servers', action='store_true',
                    help='Identify WAF')

group.add_argument('-pb', '--probe', action='store_true',
                    help='Probe Domains')

group.add_argument('-a', '--all', action='store_true',
                    help='Use all arguments')


                    
args = parser.parse_args()


with open(f"{args.urls}", "r") as f:
    domains = (x.strip() for x in f.readlines())

def ip(links):
    if "http" in links:
        links = links.replace("http://", "")
    if "https" in links:
        links = links.replace("https://", "")
    return socket.gethostbyname(links)

def PortScan(links):
    ports = ['80', '8080', '443']
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip(links), int(port)))
        if result == 0:
            return port
        else:
            pass

def get_request(urls: str) -> str:
    try:
        http = f"http://{urls}"
        https = f"https://{urls}"
        ua = UserAgent()
        header = {'User-Agent':str(ua.chrome)}  
        s = requests.Session()
        rhttp = s.get(http)
        rhttps = s.get(https)
        http_headers = rhttp.headers
        https_headers = rhttps.headers
        for value, key in http_headers.items():
            if value == "Content-Length":
                content_length = key
            if value == "Server":
                server = key
        for value, key in https_headers.items():
            if value == "Content-Length":
                content_length9 = key
            if value == "Server":
                server_ssl = key         

        if args.urls:
            if args.statuscode:               
                print(f"{Fore.GREEN}{http}{Fore.MAGENTA} - {Fore.CYAN} [{rhttp.status_code}][{content_length}]")
                print(f"{Fore.GREEN}{https}{Fore.MAGENTA} - {Fore.CYAN} [{rhttps.status_code}][{content_length9}]")
            if args.preferhttps:
                match rhttps.status_code:
                    case 200:
                        print(f"{Fore.GREEN}{https}")
            if args.servers:
                match rhttp.status_code:
                    case 200:
                        print(f"{Fore.GREEN}{http}{Fore.MAGENTA} - {Fore.CYAN}[{server}]")
                match rhttps.status_code:
                    case 200:
                        print(f"{Fore.GREEN}{https}{Fore.MAGENTA} - {Fore.CYAN}[{server_ssl}]")  
            if args.probe:
                match rhttp.status_code:
                    case 200:
                        print(f"{Fore.GREEN}{http}")
                match rhttps.status_code:
                    case 200:
                        print(f"{Fore.GREEN}{https}")   
            if args.all:
                print(f"{Fore.GREEN}{http}{Fore.MAGENTA} - {Fore.CYAN} [{rhttp.status_code}][{content_length}][{server}][{ip(http)}][{PortScan(http)}]")
                print(f"{Fore.GREEN}{https}{Fore.MAGENTA} - {Fore.CYAN} [{rhttps.status_code}][{content_length9}][{server_ssl}][{ip(https)}][{PortScan(https)}]")               

                                         
    except IndexError:
        pass
    except:
        pass

def main(domains):
    get_request(domains)


if __name__ == "__main__":
    print(f"{Fore.BLUE} {banner}")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(main, domains)




