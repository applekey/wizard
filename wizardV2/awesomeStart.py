from bottle import route, run, template,static_file,get,post
import os,sys
from threading import Thread
from win32api import GetSystemMetrics
from selenium import webdriver
import time

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
        width = GetSystemMetrics (0)
        height = GetSystemMetrics (1)
        driver = webdriver.Firefox()
        driver.set_window_size(width/2.5,height*0.95)
        driver.set_window_position(0, 0)
        time.sleep(0.3)
        driver.get('http://localhost:1234/hello')



def startUp():
    global extensions
    extensions = extensionController.getExtensions('extensions')


browser = BrowserOpen()
browser.start()
startUp()

run(host='localhost', port=1234,debug=True)
