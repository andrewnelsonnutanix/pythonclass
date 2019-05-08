# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
myindex = 0
flaverage = 0.0
mytotal = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    colonpos = line.find(':')
    spampos = line.find(' ',colonpos+2)
    strspam = line[colonpos+2:spampos]
    flspam = float(strspam)
    mytotal = mytotal + flspam
flaverage = mytotal / count
print("Average spam confidence:", flaverage)
