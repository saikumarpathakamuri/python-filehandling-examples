from zipfile import *
def creation_of_zip():
	with ZipFile("myfiles.zip","w",ZIP_DEFLATED) as f:
		f.write("ex1.py")
		f.write("sample1.txt")
if __name__ == '__main__':
	creation_of_zip()