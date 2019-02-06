#!/usr/bin/env python2

import sys, os
from time import sleep
from core.url import *
from core.colors import white, green, end, red, yellow
import urllib2
os.system("clear")
def banner():
 print """%s
\t__________         __      __      ___.    
\t\______   \___.__./  \    /  \ ____\_ |__  
\t |     ___<   |  |\   \/\/   // __ \| __ \ 
\t |    |    \___  | \        /\  ___/| \_\ \ 
\t |____|    / ____|  \__/\  /  \___  >___  / 
\t           \/            \/       \/    \/ 0.1

%s
\t           [*] Testing Tool [*]
\t         [*] Made By: Mr-z3r0 [*]
\t        [*] Download code page [*]%s
"""%(green, red, end)

def main():
 page = raw_input("%sPage >> %s"%(green, end))
 name = raw_input("%sName >> %s"%(green, end))
 check= url(page) 
 result = urllib2.urlopen(check)
 write = result.read()
 f = open(name, 'w')
 f.write(write)
 f.close()
 print "Data created!"
def control():
 try:
   while True:
     main()
     banner()
 except KeyboardInterrupt:
        print("\n[!] CTRL+C Detected, Exiting . . .")
        sleep(2)
        sys.exit()
if __name__ == "__main__":
 banner()
 main()
