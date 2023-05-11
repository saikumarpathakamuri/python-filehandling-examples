''' this is Sandesh class '''
import os
import sys

def check_file():
	filename=input("enter the file name : \t")
	if os.path.isfile(path=filename) :
		print(filename,"   :  file exists ")
		with open(filename,"r") as f:
			print(" the context present within the file ",f.name, " is follows ")
			print(f.read())
	else:
		print(filename," :  file does not exists")
		sys.exit()
		print("try again ")
if __name__ == '__main__':
	check_file()