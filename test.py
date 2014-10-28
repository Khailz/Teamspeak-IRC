__author__ = 'Khailz'

import telnetlib, socket, time, ConfigParser, time

class connection():
#login Credidentials

    config = ConfigParser.ConfigParser()
    config.readfp(open(r'info.conf'))
    username = config.get('File', 'username')
    password = config.get('File', 'password')
    host = config.get('File', 'host')
    port = config.get('File', 'port')
    timeout = 30


    def connect_server(self, host, port):
        try:
            tn = telnetlib.Telnet(host, port, connection.timeout)
        except socket.timeout:
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

