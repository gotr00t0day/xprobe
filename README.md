# xprobe
A fast HTTP multi tool for recon.


# INSTALLATION

requires Python 3.10

git clone https://github.com/gotr00t0day/xprobe.git

cd xprobe

pip3 install -r requirements.txt


# USAGE
```bash
usage: xprobe.py [-h] [-url URLS] [-sc] [-p] [-sr] [-pb] [-a]

options:
  -h, --help            show this help message and exit
  -url URLS, --urls URLS
                        Domains to probe
  -sc, --statuscode     HTTP Status Codes
  -p, --preferhttps     Display https only domains
  -sr, --servers        Identify WAF
  -pb, --probe          Probe Domains
  -a, --all             Use all arguments
```

 # EXAMPLE
 
 probe domains
 ```
 python3 xprobe.py --urls subdomains.txt --probe
 ```
 check status codes
 ```
 python3 xprobe.py --urls subdomains.txt --statuscode
 ```
 display https only domains
 ```
 python3 xprobe.py --urls subdomains.txt --preferhttps
 ```
 identify the server
 ```
 python3 xprobe.py --urls subdomains.txt --servers
 ````
  use all the arguments
 ```
 python3 xprobe.py --urls subdomains.txt --all
 ````
