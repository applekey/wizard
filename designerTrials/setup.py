from distutils.core import setup
import py2exe


Mydata_files = []
for files in os.listdir('C:/path/to/image/directory/'):
	f1 = 'C:/path/to/image/directory/' + files
	if os.path.isfile(f1): # skip directories
		f2 = 'images', [f1]
		Mydata_files.append(f2)

setup(
	windows=[{"script":"awsomeStart.py"}],
	data_files = Mydata_files, 
	options={"py2exe":{"includes":["sip"]}})