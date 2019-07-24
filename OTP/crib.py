def xored(p,k):
	return "".join([chr(ord(a)^ord(b)) for (a,b) in zip(p,k)])

def crib(text, c):
	text = text.decode('hex')
	for i in range(0, len(text) - len(c) + 1):
		slc = text[i:(i+len(c))]
		print "\t{0}: {1}".format(i,xored(slc,c))

crib("01015814471c1c171212083e3a1e3e19310832001e1008070f2b5b201c","criptografia_")