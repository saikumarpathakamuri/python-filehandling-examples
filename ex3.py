def read():
	f=open("C:\\Users\\saiku\\OneDrive\\Desktop\\PYTHON\\REGULAR EXPRESSION\\sample2.txt","r")
	print("file is opened")
	print(f.read())
	f.close()
	print("file is closed ")
if __name__ == '__main__':
	read()