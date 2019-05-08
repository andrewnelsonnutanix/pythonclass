name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

linelist = list()
counts = dict()

for line in fh:
    line.rstrip()
    linelist = line.split()
    try:
        mycatchstring = linelist[0]
    except:
        continue
    if linelist[0] == 'From':
        if linelist[1] not in counts:
            counts[linelist[1]] = 1
        else:
            counts[linelist[1]] = counts[linelist[1]] + 1
maxcount = 0
for key in counts:
    if counts[key] > maxcount:
        maxfrom = key
        maxcount = counts[key]

print (maxfrom, maxcount)
