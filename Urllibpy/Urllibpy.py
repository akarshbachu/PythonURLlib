#this is alternative to socket programming Internally it is socket programming
import urllib
fhand=urllib.urlopen('http://www.py4inf.com/code/romeo.txt');

for line in fhand:
    print line.strip();