__author__ = 'Khailz'

import telnetlib

HOST = "unlightedgaming.com"
port = 10011

tn = telnetlib.Telnet(HOST)

print tn.read_all()