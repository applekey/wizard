from bottle import route, run, template,static_file,get,post
import os

from Tkinter import *
import tkFileDialog


@route('/hello')
def hello():


	# initialize connection
	# remote = mmRemote();
	# remote.connect();

	# # construct commands to run
	# cmd = mmapi.StoredCommands()
	# cmd.AppendBeginToolCommand("offset")
	# #cmd.AppendCompleteToolCommand("accept")
	# #cmd.AppendSceneCommand_OpenMixFlie("c:\\scratch\\test1.mix");

	# # execute  commands
	# remote.runCommand(cmd);

	# #done!
	# remote.shutdown()
	print os.getcwd()
	return  static_file('index.html',root='')

@route(':path#.+#', name='static')
def static(path):
	print 'path is' +path
	return static_file(path, root='static')

@post('/api/<function>') # or @route('/login', method='POST')
def importMesh(function):
	print 'function is' + function
	root = Tk()
	root.withdraw()
	fileName= str(tkFileDialog.askopenfilename(parent=root,filetypes=[("3d Files","*.ply;*.obj")]))



run(host='localhost', port=1234,debug=True)
