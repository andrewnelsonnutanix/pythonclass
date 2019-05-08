name = input('Enter a filename:')
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
linelst = list()
timelst = list()
hourdict = dict()
delimiter =':'
for line in fh:
    line = line.rstrip()
    linelst =line.split()
    if linelst == []:
        continue
    if linelst[0] == 'From':
        timelst = linelst[5].split(delimiter)
        hour = timelst[0]
        if hour not in hourdict:
            hourdict[hour] = 1
        else:
            hourdict[hour] = hourdict[hour] + 1

tmp = list()
for k,v in hourdict.items() :
    newt = (k,v)
    tmp.append (newt)

tmp = sorted(tmp)
for k,v in tmp :
    print(k,v)
