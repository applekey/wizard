from bottle import route, run, template,static_file,get
import os



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


# # Static Routes
# @get('/<filename:re:.*\.js>')
# def javascripts(filename):
#     return static_file(filename, root='static/js')

# @get('/<filename:re:.*\.css>')
# def stylesheets(filename):
#     return static_file(filename, root='static/css')

# @get('/<filename:re:.*\.(mp4|avi)>')
# def video(filename):
	
# 	return static_file(filename, root='static/img')

# @get('/<filename:re:.*\.(jpg|png|gif|ico)>')
# def images(filename):
# 	print 'want filename' + filename
# 	return static_file(filename, root='static/img')

# @get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
# def fonts(filename):
#     return static_file(filename, root='static/fonts')

@route(':path#.+#', name='static')
def static(path):
	print 'path is' +path
	return static_file(path, root='static')



run(host='localhost', port=1234,debug=True)
