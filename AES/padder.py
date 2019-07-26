from pwn import *
conn = process(['python','server.py'])

print(conn.recvuntil(":"))

for i in range(64,256):
	char = chr(i)
	text = "}"+char * 31
	send_text = text+"a"
	conn.sendline(send_text)
	conn.recvline()
	code = conn.recvline()
	c1, c2, c3 = code[:64], code[64:128], code[128:192]
	if(c1 == c3):
		paddingChar = char
		break
	conn.recvline()
print("El padding se esta realizando con: "+paddingChar)

flag = ""
for i in range(31):
	for j in range(32,127):
		char = chr(j)
		text = char + flag + paddingChar * (31-i)
		send_text = text+"a"+"a"*i
		conn.recvuntil(":")
		conn.sendline(send_text)
		conn.recvline()
		code = conn.recvline()
		c1, c2, c3 = code[:64], code[64:128], code[128:192]
		if(c1 == c3):
			flag = char + flag
			print(flag)
			break
		conn.recvline()

print("La bandera es: " + flag)