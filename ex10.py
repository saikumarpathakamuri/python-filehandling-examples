def read():
	f=open("sample9.txt","r")
	data=f.read(9)
	print(data)
	print(type(data))
	f.close()
if __name__ == '__main__':
	read()