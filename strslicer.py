mystring = None
text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
ipos = text.find(':')
mystring = text[pos:pos+6]
piece = text[ipos+1:]
piece.strip()
fvar = float(mystring)
print (fvar)
