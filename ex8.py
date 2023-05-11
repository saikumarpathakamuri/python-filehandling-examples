def writelines_operations1():
	f=open(file="sample8.txt",mode="w")
	print("file is opened")
	list=["sandesh","vishruth","suhas"]
	f.writelines(list)
	f.close()
	print("file got closed")
def writelines_operations2():
	f=open(file="sample9.txt",mode="w")
	print("file is opened")
	list=["sandesh\n","vishruth\n","suhas"]
	f.writelines(list)
	f.close()
	print("file got closed")

if __name__ == '__main__':
	writelines_operations1()
	writelines_operations2()