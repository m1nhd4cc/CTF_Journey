
import hashlib
import string

with open("hardcore.bnk", "rb") as f:
	data = f.read()

charset = string.ascii_letters + string.digits + string.punctuation

def check(flag):
	print(flag)
	return hashlib.md5(flag.encode()).digest() not in data

def search(flag):
	if len(flag) == 62:
		return True
	
	for char in charset:
		if check(flag + char):
			if search(flag + char):
				return True
	return False

search("")