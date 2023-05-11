def tell_operation():
	with open("sample15.txt","r") as f:
		print(f.tell())
		print(f.read(3))
		print(f.tell())
		print(f.read(3))
		print(f.tell())
		print(f.read(3))
		print(f.tell())
		print(f.read(3))
		print(f.read(-1))
if __name__ == '__main__':
	tell_operation()