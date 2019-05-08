fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
linelst = []

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    linelst =line.split()
    if linelst == []:
        continue
    if linelst[0] == 'From':
        print (linelst[1])
    if linelst[0] == 'From':
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
