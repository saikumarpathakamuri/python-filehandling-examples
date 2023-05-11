def readlines1():
	f=open("sample11.txt","r")
	lines=f.readlines()
	print(lines)
	print(type(lines))
	for line in lines:
		print(line,end="")
def readlines2():
	f=open("sample11.txt","r")
	lines=f.readlines(1)
	print(lines)
	print(type(lines))
	for line in lines:
		print(line,end="")
if __name__ == '__main__':
	readlines1()
	readlines2()