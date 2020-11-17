from datetime import datetime

dat = str(datetime.today()).split()
hour = dat[1].split(".")

from json import load

from urllib import request

urlopen = request.urlopen
ip = load(urlopen('http://jsonip.com'))['ip']

print ('____________________________________\n') 

print ('DATE:                ' +  dat[0] )

print( '____________________________________') 

print( '\nTIME:                ' + hour[0])

print( '____________________________________') 

print( '\nIP ADDRESS:          ' + ip)

print( '____________________________________\n\n' )


print('\n Pavan The Hacker !')
