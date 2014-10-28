from distutils.core import setup
from test import connection
import py2exe

Mydata_files = connection.config_file

setup(
     console=['C:/Users/311student/PycharmProjects/Teamspeak-IRC/test.py'],
     data_files = Mydata_files,
     options={
                 "py2exe":{
                         "unbuffered": True,
                         "optimize": 2,
                         "excludes": ["email"]
                 }
         }
 )