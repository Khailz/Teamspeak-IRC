__author__ = 'Khailz'

import os, shutil, telnetlib, socket, ConfigParser, time

config_file = os.path.realpath('config/info.cfg')
example_file = os.path.realpath('config/info.cfg.sample')

if not os.path.exists('config'):
    os.makedirs('config')

if os.path.isfile(config_file):
    pass
else:
    shutil.copy(example_file, 'config')




class connection():
    #login Credidentials
    config = ConfigParser.ConfigParser()
    config.readfp(open(r"config/info.cfg"))
    username = config.get('CONFIG', 'username')
    password = config.get('CONFIG', 'password')
    host = config.get('CONFIG', 'host')
    port = config.get('CONFIG', 'port')
    timeout = 30

    #def invalid_cfg(self):

        #if config_file("username="):






    def connect_server(self, host, port):
        try:
            tn = telnetlib.Telnet(host, port, connection.timeout)
        except socket.timeout:
            print ("socket timeout")
        except socket.error:
            print ("socket error")
        else:
            tn.write("login %s %s\n" % (connection.username, connection.password))
            print "Succesfully Logged in!\n"
            time.sleep(1)
            tn.write("use 1\n")
            print "Using 1..\n"
            time.sleep(1)
            tn.write("clientupdate client_nickname=Admin\n")
            print "Updating name...\n"
            time.sleep(1)
            tn.write("clientpoke clid=9 msg=Connected\n")
            print "Testing poke...\n"
            time.sleep(1)
            tn.write("servernotifyregister event=textprivate\n")
            print "Accepting messages!\n"
            time.sleep(1)
            tn.write("gm msg=Bot\sConnected!\n")
            print "Global Message for succesful bot connection sent!\n"
            tn.write("%s" % commands.command1)
            print tn.read_eager()

            while True:
                print tn.read_until("notifytextmessage targetmode=1 msg=")

            #tn.read_all#("notifytextmessage targetmode=1 msg=", timeout=20)

class commands():

    command1 = ("gm msg=Hi\n")

    def get_user_uuid(self):

        """
This will recieve user ID and UUID
from teamspeak and convert it to a
variable.

        """
        user


connection().connect_server(connection.host, connection.port)





