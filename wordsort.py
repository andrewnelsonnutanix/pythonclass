fname = input("Enter file name: ")
fh = open(fname)
lstmaster = ['hello','there']
lstpresort = []
count = 0

for line in fh:
    line = line.rstrip()
    lstpresort = line.split()
    for x in range(len(lstpresort)):
        neword = lstpresort[x]
        lstmaster.append(neword)

#lstmaster = lstmaster.sort()
for i in range(len(lstmaster)):
    print (lstmaster[i])
