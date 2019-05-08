def computepay(h,r):
	if h <= 40 :
		p = h * r
	elif h > 40 :
		p = ((h-40) * 1.5 * r) + 40 * r
	else :
		p = 0
	return p

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try :
	fhrs = float(hrs)
	frate = float(rate)
except :
	print ("Invalid input")
p = computepay(fhrs,frate)
print(p)
