from bottle import route, run, template,static_file,get,post
import os,sys

sys.path.append( 'extensionController' )
sys.path.append( 'meshController' )
sys.path.append( 'meshController/implementation' )
sys.path.append( 'meshController/pythonApi' )

from extensionController import *
from MeshWrapper import  *

@route('/hello')
def hello():
	return  static_file('index.html',root='')

@route(':path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@post('/api/<function>') # or @route('/login', method='POST')
def importMesh(function):
	callDynamic(function)
	

def callDynamic(functionCall):
    try:
       index = functionCall.index('(')
       functionName = functionCall[0:index]
       for method in extensions:
           if hasattr(method, functionName):
               if eval('method.'+functionCall) is not True:
                   print 'error'
                   return
               else:
                   return
                   
       print 'error couldnt find'         
    except ex:
        print ex
        print 'error'


def startUp():
    global extensions
    extensions = extensionController.getExtensions('extensions')
    print extensions


startUp()
run(host='localhost', port=1234,debug=True)
