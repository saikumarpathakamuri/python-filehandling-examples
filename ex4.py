def properties():
	f=open("sample4.txt")
	print(f.read(+))
	print(f.name)
	print(f.mode)
	print(f.readable())
	print(f.writable())
	print(f.closed)
	f.close()
	print(f.closed)
if __name__ == '__main__':
	properties()