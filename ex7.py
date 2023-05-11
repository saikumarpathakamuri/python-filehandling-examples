def write_operations():
	f=open(file="sample7.txt",mode="a")
	f.write("my name\n")
	f.write("is\n")
	f.write("saikumarpathakamuri\n")
	f.write("django\n")
	f.write("python\n")
	f.write("Sandesh\n")
	print(f.name)
	f.close()
if __name__ == '__main__':
	write_operations()
