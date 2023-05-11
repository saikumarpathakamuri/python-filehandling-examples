def with_statement():
	with open("sample14.py","w") as f:
		f.write("Sandesh\n")
		f.write("will teach\n")
		f.write("Django")
		print(f.name)
		print(f.closed)
	print(f.closed)
if __name__ == '__main__':
	with_statement()