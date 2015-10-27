#!/usr/bin/python

from socket import *
import sys, time
from datetime import datetime
import Queue
from threading import Thread

host = ''
max_port = 1
min_port = 1

def hilite(string, status, bold):
        attr = []
        if status:
                # green
                attr.append('32')
        else:
                # red
                attr.append('31')
        if bold:
                attr.append('1')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)

def scan_host(host, port, r_code = 1):
        try:
                s = socket(AF_INET, SOCK_STREAM)
                code = s.connect_ex((host, port))

                if code == 0:
                        r_code = code
                s.close()
        except Exception, e:
                pass
        return r_code

try:
	host = raw_input("[*] Enter Target Host Address: ");
	min_port = int(raw_input("[*] Enter the starting port: "));
	max_port = int(raw_input("[*] Enter the ending port: " ));
except KeyboardInterrupt:
	print("\n\n[*] User Requested An Interrupt.")
        print("[*] Application Shutting Down.")
        sys.exit(1)

open_ports = list()
hostip = gethostbyname(host)
print("\n[*] Host: %s IP: %s" % (host, hostip))
print("[*] Scanning started At %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port + 1):
        try:
                response = scan_host(host, port)

                if response == 0:
                        print(hilite("[*] Port %d: Open" % (port), True, False))
                        open_ports.append(port)
                else:
                        print(hilite("[*] Port %d: Closed" % (port), False, False))
        except Exception, e:
                pass

stop_time = datetime.now()
