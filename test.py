__author__ = 'Khailz'

import os, telnetlib, socket, time, ConfigParser, time

os.chdir('C:/Users/311student/PycharmProjects/Teamspeak-IRC')

class connection():
#login Credidentials

    config_file = "info.cfg"
    config = ConfigParser.ConfigParser()
    config.readfp(open(r'info.cfg'))
    username = config.get('CONFIG', 'username')
    password = config.get('CONFIG', 'password')
    host = config.get('CONFIG', 'host')
    port = config.get('CONFIG', 'port')
    timeout = 30


    def connect_server(self, host, port):
        try:
            tn = telnetlib.Telnet(host, port, connection.timeout)
        except socket.timeout:
            print ("socket timeout")
        except socket.error:
            print ("socket timeout")
        else:
            tn.write("login %s %s\n" % ("serveradmin", "mikhail9"))
            tn.write("use 1\n")
            tn.write("clientupdate client_nickname=Admin\n")
            tn.write("clientpoke clid=2 msg=Connected\n")
            tn.write("servernotifyregister event=textprivate\n")
            tn.write("gm msg=Bot\sConnected!\n")
            tn.read_until("notifytextmessage targetmode=1 msg=", timeout=9999)




connection().connect_server("unlightedgaming.com", "10011")

