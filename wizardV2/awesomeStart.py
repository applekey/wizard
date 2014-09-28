from bottle import route, run, template,static_file,get,post
import os,sys
from threading import Thread
import time
import webbrowser

sys.path.append( 'extensionController' )
sys.path.append( 'meshController' )
sys.path.append( 'meshController/implementation' )
sys.path.append( os.path.join('meshController','pythonApi') )

from extensionController import *
from MeshWrapper import  *

@route('/index')
def hello():
	return  static_file('index.html',root='')
@route('/boot')
def hello():
	return  static_file('boot.html',root='')

@route(':path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@post('/api/<function>') # or @route('/login', method='POST')
def importMesh(function):
	return callDynamic(function)

@post('/history/check') # or @route('/login', method='POST')
def checkPast():
    if os.path.isdir('/history'):
        for root, dirs, files in os.walk("/history"):
            for file in files:
                if file.endswith(".mix"):
                    return file

@post('/history/loadLatest') # or @route('/login', method='POST')
def getLatest():
    print callDynamic('importFigure()')

	

def callDynamic(functionCall):
    try:
       index = functionCall.index('(')
       functionName = functionCall[0:index]
       for method in extensions:
           if hasattr(method, functionName):
               call = 'method.'+functionCall
               if eval(call) is not True:
                   return 'false'
               else:
                   return 'true'
                          
    except :
        return 'false'

class BrowserOpen(Thread):

    def run(self):
        global myport 
        myport = 1343
        global url
        url = 'http://localhost:' +str(myport)+'/boot'
        webbrowser.open(url,new=1,autoraise=True)
     
def startUp():
    global extensions
   
    extensions = extensionController.getExtensions('extensions')


browser = BrowserOpen()
browser.start()
startUp()

print 'Semaphore MeshMixer Controller is now working at' 
print str(url)
print "Please don't close this window"
run(host='localhost', quiet=True,port=myport,debug=False)
