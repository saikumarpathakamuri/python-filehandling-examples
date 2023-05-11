from zipfile import *
def unzipping():
 	with ZipFile("myfiles.zip","r",ZIP_STORED) as f:
 		names=f.namelist()
 		print(names)
if __name__ == '__main__':
 	unzipping()