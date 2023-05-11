def read1():
	f=open("sample11.txt","r")
	line1=f.readline()
	print(line1)
	line2=f.readline()
	print(line2)
	line3=f.readline()
	print(line3)
def read2():
	f=open("sample11.txt","r")
	line1=f.readline()
	print(line1,end="")
	line2=f.readline()
	print(line2,end="")
	line3=f.readline()
	print(line3)

	f.close()
if __name__ == '__main__':
	read1()
	read2()