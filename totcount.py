mytotal = 0
mycount = 0.0

while True :
    sval = print("Enter a number:")
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print ("Invalid Input")
        continue
    mycount = mycount + 1
    mytotal = mytotal + fval

#print ("All done")
print (mytotal,mycount,mytotal/mycount)
