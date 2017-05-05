#!/usr/bin/python
import socket

import config
import tailer

server_addr = config.server['host']
server_port = config.server['port']
logfile = config.log['path']
myname = config.node['name']
streamid = config.log['streamid']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_addr, server_port))
print "Going to send data to " + server_addr + ":" + str(server_port)

s.send('+node|' + str(myname) + '|' + str(streamid) + '\r\n')

for line in tailer.follow(open(logfile)):
    data = '+log|' + str(streamid) + '|' + str(myname) + '|info' + '|' + line + '\r\n'
    s.send(data)

# unregister me
# s.send('-node|'+str(myname)+'\r\n')

s.close()
