import re

urlstring = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
print (urlstring)
href = re.findall('href="(.+)"', urlstring)
print (href)
