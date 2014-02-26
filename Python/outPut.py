#NIE ZAPOMNIJ 0x I ""!
def htb(heks):
	l = bin(int(heks, 16))[2:].zfill(8)
	return l
print(htb("0xab"))
print(htb("0xcd"))
print(htb(str(0xde and 0xad)))
print(htb("0x01"))

