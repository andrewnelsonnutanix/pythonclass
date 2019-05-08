import re

name = input('Enter a filename:')
if len(name) < 1 : name = "regex_sum_138242.txt"
fh = open(name)
perline = list()
lst = list()
linesum = 0

for line in fh:
    line = line.rstrip()
    perline = re.findall('[0-9]+', line)
    for x in perline :
        myintx = int(x)
        linesum = linesum + myintx
    lst.append(linesum)
    linesum = 0

sum = 0
print(lst)
for y in lst :
    myinty = int(y)
    sum = sum + myinty
print (sum)
