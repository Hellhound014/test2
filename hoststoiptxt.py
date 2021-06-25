#!/usr/bin/python
import sys, socket
f = open(sys.argv[1])
for i in f:
    i = i.rstrip()
    try:
        ip = socket.gethostbyname(i)
    except:
        ip = "Doesn't resolve"
    print(i + " -> " + ip)
	
	#test