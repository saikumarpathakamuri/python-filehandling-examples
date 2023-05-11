''' this is Sandesh class '''
import os
import sys

def check_file():
	filename=input("enter the file name : \t")
	if os.path.isfile(path=filename) :
		print(filename,"   :  file exists ")
		with open(filename,"r") as f:
			l=0
			c=0
			w=0
			for i in f:
				l=l+1
				c=len(i)+c
				words=i.split()
				w=w+len(words)
		print("no of lines ",l)
		print("no of words ",w)
		print("no of characters ", c)
	else:
		print(filename," :  file does not exists")
		sys.exit()
		print("try again ")
if __name__ == '__main__':
	check_file()