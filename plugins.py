#!/usr/bin/python
'coded by l314ck_h4ck3l2 '

import os
import sys
import time
import requests


blue = '\033[34m'
green = '\033[32m'
red = '\033[31m'
yellow = '\033[33m'
error = '\033[91m'
cyan = '\033[36m'
bold    = "\033[;1m"
reset = "\033[0;0m"

path = 'plugins_list.txt'
plugins = open(path , 'r').read().splitlines()

def banner():
    print(f"""{blue}

        ___   __                      __                     
       F _ ", LJ   _    _     ___ _   LJ   _ ___      ____   
      J `-' | FJ  J |  | L   F __` L      J '__ J    F ___J  
      |  __/FJ  L | |  | |  | |--| |  FJ  | |__| |  | '----_ 
      F |__/ J  L F L__J J  F L__J J J  L F L  J J  )-____  L
     J__|    J__LJ\____,__L )-____  LJ__LJ__L  J__LJ\______/F
     |__L    |__| J____,__FJ\______/F|__||__L  J__| J______F 
                           J______F                         

 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{cyan}
 ~                   Author : l314ck_h4ck3l2                   ~
 ~          github : https://github.com/l314ck-h4ck3l2         ~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{reset}""")

def discover_plugins(site):
    try:
        req = requests.get(site)
    except requests.ConnectionError:
        print(f'{red} [!] Host is Not True !{reset}')
        sys.exit()
    if  req.status_code == 200:
        for plugin in plugins:
            url = site + plugin
            try:
                res = requests.get(url)
                print(f'{green} [+] {url}{reset}')
                time.sleep(0.5)
            except requests.ConnectionError:
                print(f'{red} [-] {url}{reset}')
                time.sleep(0.5)

def usage():
    print(f'{error} Usage   : python Plugins.py [url]{reset}')
    print(f'{error} Example : python Plugins.py instagram.com{reset}')
    print(f'{error} Example : python Plugins.py https://www.instagram.com{reset}')
    sys.exit()

def main():
    os.system('cls' or 'clear')
    banner()
    if len(sys.argv) == 2:
        if sys.argv[1].startswith('http://www.'):
            domain = sys.argv[1][11:]
            site = sys.argv[1] + '/wp-content/plugins/'
        elif sys.argv[1].startswith('https://www.'):
            domain = sys.argv[1][12:]
            site = sys.argv[1] + '/wp-content/plugins/'
        else:
            domain = sys.argv[1]
            site = 'http://www.' + domain + '/wp-content/plugins/' or 'https://www.' + domain + '/wp-content/plugins/'
        print(f'{yellow} domian : {domain}{reset}')
        print(f'{yellow} site : {site}{reset}')
        print()
        discover_plugins(site)
    else:
        usage()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
