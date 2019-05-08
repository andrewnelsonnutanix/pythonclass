largest = None
smallest = None
sval = None
ival = 0
mycount = 0

while True :
    sval = input("Enter a number:")
    if sval == 'done' :
        break
    try :
        ival = int(sval)
    except :
        print ("Invalid input")
        continue
    if mycount == 0:
        smallest = ival
    if ival > largest :
        largest = ival
    if ival < smallest :
        smallest = ival
    mycount = mycount + 1

print("Maximum is", largest)
print("Minimum is", smallest)
