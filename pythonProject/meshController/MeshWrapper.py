import os,sys
sys.path.append( 'meshController/implementation' )
sys.path.append( 'meshController/pythonApi' )

import mmapi
from mmRemote import *

class MeshWrapper(object):  
    @staticmethod
    def SingleInstanceApiCommander(operation, modifier, modifierValue):
        try:
            remote = mmRemote()
            remote.connect()
            cmd = mmapi.StoredCommands()
            #some commands don't follow the scheme

            if operation is "open":
                cmd.AppendSceneCommand_OpenMixFile(modifier)
            elif operation is "selectAll":
                 cmd.AppendSelectCommand_All()
            else:
                cmd.AppendBeginToolCommand(operation)
        
            if modifierValue is not None:
                cmd.AppendToolParameterCommand(modifier,modifierValue)
                #cmd.AppendCompleteToolCommand("accept")

        
            remote.runCommand(cmd);
            remote.shutdown();
        except:
            pass
            #to do log this
        finally:
            remote.shutdown();
    @staticmethod
    def importFigure(fileLocation):
        MeshWrapper.SingleInstanceApiCommander("open",fileLocation,None)

    @staticmethod
    def selectAll(): 
      MeshWrapper.SingleInstanceApiCommander("selectAll",None,None)

    @staticmethod
    def wireframe():
        print 'here'

    @staticmethod
    def remesh(value):
       MeshWrapper.SingleInstanceApiCommander("remesh","smooth",value)

    @staticmethod
    def deformsmooth(value):
       MeshWrapper.SingleInstanceApiCommander("smooth","scale",value)
     
    @staticmethod
    def roughtselectionforsocket():
        print 'here'
    
    @staticmethod
    def invertSelection():
        print 'here'

    @staticmethod
    def editoffset(value):
        MeshWrapper.SingleInstanceApiCommander("offset","distance",value)

    @staticmethod
    def ModifySmoothBoundary(value):
        MeshWrapper.SingleInstanceApiCommander("smoothboundary","smoothness",value)

    @staticmethod
    def editDiscard():
        MeshWrapper.SingleInstanceApiCommander("discard",None,None)


    @staticmethod
    def selectleghide():
        print 'here'

 
