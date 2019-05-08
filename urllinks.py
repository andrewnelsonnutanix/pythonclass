# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

localcount = 0
totalcount = 1
localposition = 0
totalposition = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
strcount = input('Enter count: ')
totalcount = int(strcount)
strposition = input('Enter position: ')
totalposition = int(strposition)

totalposition = totalposition - 1

while localcount < totalcount :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find_all('a'):
        if localposition == totalposition :
            url = link.get('href')
        localposition = localposition + 1
    localposition = 0
    localcount = localcount + 1
print (url)
