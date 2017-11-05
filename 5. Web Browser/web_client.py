#!/usr/bin/python

from urlparse import urlparse
import socket
import sys

hostname = urlparse(sys.argv[1]).netloc
path = urlparse(sys.argv[1]).path

server_address = (hostname, 80)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)
string = "GET " + path + " HTTP/1.1\r\nHost:" + hostname + "\r\nConnection:close\r\n\r\n"
sock.send(string)
#print "GET Request header:"
print string

content = ''
while True:
    data = sock.recv(1024)
    if data:
        content += data
    else:
        break

l = len(content)
clist = content.split()

if 'Content-Length:' in clist:
    index = clist.index('Content-Length:')
    cl = int(clist[index+1])

else:
    cl = -1

if cl != -1:
    #print 'GET Response header:'
    print content[0:l-cl]
    newfile = open(sys.argv[2], 'w')
    newfile.write(content[l-cl:])
    newfile.close()
else:
    print 'No content-length in HEAD'








