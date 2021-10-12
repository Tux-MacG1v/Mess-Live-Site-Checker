import socket
from multiprocessing.dummy import Pool as ThreadPool
import sys,os,re,socket,binascii,time,json,random,threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path,hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal,base64,colorama,requests
from colorama import *
from random import choice
from colorama import Fore,Back,init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from Queue import Queue
from time import strftime
from urlparse import urlparse
from urllib2 import urlopen
colorama.init()

# Now regular ANSI codes should work, even in Windows
CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"   # mode 31 = red forground
RESET = "\033[0m"  # mode 0  = reset
BLUE  = "\033[34m"
YELLOW = "\033[1;33m"
CYAN  = "\033[36m"
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD    = "\033[m"
REVERSE = "\033[m"
WHITE = "\033[1;37m"

def logo():
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37  ]

        x = """ 


 _       _                _______ _                 _                 
| |     (_)              (_______) |               | |                
| |      _ _   _ _____    _      | |__  _____  ____| |  _ _____  ____ 
| |     | | | | | ___ |  | |     |  _ \| ___ |/ ___) |_/ ) ___ |/ ___)
| |_____| |\ V /| ____|  | |_____| | | | ____( (___|  _ (| ____| |    
|_______)_| \_/ |_____)   \______)_| |_|_____)\____)_| \_)_____)_|  (WEBSITE)    v.3
                  
		CODED BY TUX-MACG1V		  
											   				  
				  
				  
			                  """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)
logo()

red = '\033[0;37;41m'
green = '\033[0;37;42m'
white = '\033[00m'


def site(sites):
    try:
        sites = sites.replace('\n', '').replace('\r', '')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.20)
        result = sock.connect_ex((sites, 80))
        if str(result) != '0':
            print RED + '[-]' + WHITE + 'DEAD SITE --> ' + red + sites + '  '
        if str(result) == '0':
            print GREEN + '[+]' + WHITE + 'Live SITE --> ' + green + sites + '  '
            open("Livesites.txt", "a").write(sites + "\n")
    except:
        pass


Listsites = open(raw_input(GREEN + '['+ WHITE +'>'+ GREEN +']' + RED +'Input SITE lists:'+ WHITE +'~# '), 'r').readlines()
Thread = raw_input(GREEN + '['+ WHITE +'>'+ GREEN +']' + RED +'Thread :'+ WHITE +'~# ')
pool = ThreadPool(int(Thread))
pool.map(site, Listsites)
pool.close()
pool.join()

if __name__ == '__main__':
    print("Finished, success , Thank you for using.")
