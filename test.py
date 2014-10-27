__author__ = 'Khailz'

import telnetlib

host = "unlightedgaming.com"
port = 10011

tn = telnetlib.Telnet(host, port, timeout=5)

tn.read_until("login: ")
tn.write("login serveradmin mikhail9")

print tn.read_all()