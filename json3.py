import json
from urllib.request import urlopen

import ssl
mytotal = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
myjson = urlopen(url, context=ctx).read()

info = json.loads(myjson)

for item in info["comments"]:
#    print(item['count'])
    mycount = int(item['count'])
    mytotal = mytotal + mycount

print ('Sum:', mytotal)
