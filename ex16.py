def operation_seek():
	data="you are learning python from sandesh "
	with open("simple16.txt","w") as k:
		k.write(data)
		print(k.name)

	with open("simple16.txt","r+") as k:
		data=k.read()
		print(data)
		print(k.tell())
		k.seek(29)
		print(k.tell())
		k.write("SANDESH H S")
		k.seek(0)
		print(k.tell())
		print(k.read())


if __name__ == '__main__':
	operation_seek()