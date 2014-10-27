__author__ = 'Khailz'

user_nam = raw_input('username> ')
filename = raw_input('> ')
target = open(filename, 'w')
target.write('user_name= %s' % user_nam)
