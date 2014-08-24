import os,sys

from mmapi import  *
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
            return True
        except :
            abc =1
            #to do log this
            return False
        finally:
            remote.shutdown();
    @staticmethod
    def importFigure(fileLocation):
        return MeshWrapper.SingleInstanceApiCommander("open",fileLocation,None)

    @staticmethod
    def selectAll(): 
      return MeshWrapper.SingleInstanceApiCommander("selectAll",None,None)

    @staticmethod
    def wireframe():
        print 'here'

    @staticmethod
    def remesh(value):
       return MeshWrapper.SingleInstanceApiCommander("remesh","smooth",value)

    @staticmethod
    def deformsmooth(value):
       return MeshWrapper.SingleInstanceApiCommander("smooth","scale",value)
     
    @staticmethod
    def roughtselectionforsocket():
        print 'here'
    
    @staticmethod
    def invertSelection():
        print 'here'

    @staticmethod
    def editoffset(value):
        return MeshWrapper.SingleInstanceApiCommander("offset","distance",value)

    @staticmethod
    def ModifySmoothBoundary(value):
        return MeshWrapper.SingleInstanceApiCommander("smoothboundary","smoothness",value)

    @staticmethod
    def editDiscard():
        return MeshWrapper.SingleInstanceApiCommander("discard",None,None)


    @staticmethod
    def selectleghide():
        print 'here'

 
