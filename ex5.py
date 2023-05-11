def write_operations():
	f=open(file="sample5.txt",mode="w")
	f.write("my name")
	f.write("is")
	f.write("saikumarpathakamuri")
	print(f.name)
	f.close()
if __name__ == '__main__':
	write_operations()
