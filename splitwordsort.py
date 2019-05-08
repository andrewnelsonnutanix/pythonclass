fname = input("Enter file name: ")
fh = open(fname)
lstmaster = []
lstpresort = []

count = 0
for line in fh:
    line = line.rstrip()
    lstpresort = line.split()

    for word in lstpresort:
        if word not in lstmaster:
            lstmaster.append(word)

lstmaster.sort()
print (lstmaster)
