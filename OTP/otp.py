import sys

def xored(p,k):
	return "".join([chr(ord(a)^ord(b)) for (a,b) in zip(p,k)])

if len(sys.argv[1]) != len(sys.argv[2]):
	print "La llave y el texto a cifrar deben tener el mismo tamanio"
	exit(616)

print xored(sys.argv[1],sys.argv[2]).encode("hex")