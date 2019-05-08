import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'
sum = 0


address = input('Enter url: ')

#print('Retrieving', url)
uh = urllib.request.urlopen(address)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for eachcount in counts :
    #print (eachcount.text)
    intcount = int(eachcount.text)
    sum = sum + intcount

print (sum)
