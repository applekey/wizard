from bottle import route, run, template,static_file,get,post,request,BaseResponse
import os,sys
from threading import Thread
import time
import webbrowser
import json
import win32ui
import re
##some imports to make pyinstaller work


web = False

if web == False:
    sys.path.append( 'extensionController' )
    sys.path.append( 'meshController' )
    sys.path.append( 'meshController/mm' )
    sys.path.append( os.path.join('meshController','pythonApi') )
    from extensionController import *
    from MeshWrapper import  *
    from connector import *



@route('/index')
def hello():
	return  static_file('index.html',root='')
@route('/boot')
def hello():
	return  static_file('boot.html',root='')



def streamMediaFile(filePath):
  realpath = os.getcwd()
  realpath= os.path.join(realpath,'static')
  filePath = filePath.replace('/','\\')
  realpath =realpath+filePath
  print realpath
  range_header = request.headers.get('Range')
  size = os.path.getsize(realpath)    
  byte1, byte2 = 0, None
  
  m = re.search('(\d+)-(\d*)', range_header)
  g = m.groups()
  
  if g[0]: byte1 = int(g[0])
  if g[1]: byte2 = int(g[1])

  length = size - byte1
  if byte2 is not None:
      length = byte2 - byte1
  
  data = None
  with open(realpath, 'rb') as f:
      f.seek(byte1)
      data = f.read(length)
  
  rv = HTTPResponse(data, 206)
  rv.add_header('Content-Range','bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))
  rv.add_header('Content-Type','video/mp4')
  rv.add_header('Content-Length',length)
  #rv.headers.set('Content-Range', 'bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))
  print rv
  return rv

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

def checkifMeshMixerRunning():
  try:
    win32ui.FindWindow("QWidget", None)
    return True
  except:
    print 'meshmixer isnt open'
    return False
  
def callDynamic(functionCall):
    if not checkifMeshMixerRunning():
      return 'false'
    try:
       index = functionCall.index('(')
       functionName = functionCall[0:index]
       for method in extensions:
           if hasattr(method, functionName):
               call = 'method.'+functionCall
               result = eval(call)
               if result is True:
                   return 'true'
               elif result is False:
                   return 'false'
               else:
                  return result
                          
    except :
        return 'false'

class BrowserOpen(Thread):

    def run(self):
        global myport 
        myport = 1343
        global url
        url = 'http://localhost:' +str(myport)+'/boot'
        # webbrowser.open(url,new=1,autoraise=True)
     
def startUp():
    global extensions
    extensions = extensionController.getExtensions('extensions')


browser = BrowserOpen()
browser.start()

if web == False:
    startUp()

print 'Semaphore MeshMixer Controller is now working at' 
print str(url)
print "Please don't close this window"
print 'blah'
run(host='localhost', quiet=True,port=myport,debug=True)
