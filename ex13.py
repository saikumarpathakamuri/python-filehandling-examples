def read():
	f=open("sample11.txt")
	print(f.read(3))
	print(f.readline())
	print(f.read(5))
	print(f.readlines())
	f.close()
if __name__ == '__main__':
	read()