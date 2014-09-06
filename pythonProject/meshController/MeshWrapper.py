import os,sys

from mmapi import  *
from mmRemote import *
import implementation


class MeshWrapper(object):  
    @staticmethod
    def SingleInstanceApiCommander(operation, modifier, modifierValue):
        try:
            remote = mmRemote()
            remote.connect()
            cmd = mmapi.StoredCommands()
            #some commands don't follow the scheme

            if operation is "open":
                cmd.AppendSceneCommand_AppendMeshFile(modifier);
            elif operation is "selectAll":
                 cmd.AppendSelectCommand_All()
            elif operation is "autoRepair":
                 cmd.AppendSelectCommand_All()
            elif operation is "complete":
                cmd.AppendCompleteToolCommand("accept")
            elif operation is "cancel":
                cmd.AppendCompleteToolCommand("cancel")
            else:
                cmd.AppendBeginToolCommand(operation)
        
            if modifierValue is not None:
                cmd.AppendToolParameterCommand(modifier,modifierValue)
                #cmd.AppendCompleteToolCommand("accept")

        
            remote.runCommand(cmd);
            remote.shutdown();
            return True
        except :
            #to do log this
            return False
        finally:
            remote.shutdown();
    @staticmethod
    def planecut():
        return MeshWrapper.SingleInstanceApiCommander("planeCut",None,None) 
            
    @staticmethod
    def createFaceGroup():
        return MeshWrapper.SingleInstanceApiCommander("createFaceGroup",None,None) 
    @staticmethod
    def align():
        return MeshWrapper.SingleInstanceApiCommander("align",None,None) 
    @staticmethod
    def inspector():
        return MeshWrapper.SingleInstanceApiCommander("inspector","contactTolerance",0.3) 
    @staticmethod 
    def cancel():
        return MeshWrapper.SingleInstanceApiCommander("cancel",None,None) 
    @staticmethod 
    def complete():
        return MeshWrapper.SingleInstanceApiCommander("complete",None,None) 
    @staticmethod
    def importFigure(fileLocation):
        return MeshWrapper.SingleInstanceApiCommander("open",fileLocation,None)
    
    @staticmethod
    def smoothBoundary(): 
      return MeshWrapper.SingleInstanceApiCommander("smoothboundary","smoothness",40)
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

 
