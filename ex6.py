def write_operations():
	f=open(file="sample6.txt",mode="w")
	f.write("my name\n")
	f.write("is\n")
	f.write("saikumarpathakamuri")
	print(f.name)
	f.close()
if __name__ == '__main__':
	write_operations()
