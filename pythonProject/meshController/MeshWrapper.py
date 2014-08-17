import os
import sys
sys.path.append( 'meshController/implementation' )
sys.path.append( 'meshController/pythonApi' )

import mmapi
from mmRemote import *

class MeshWrapper(object):  
    @staticmethod
    def SingleInstanceApiCommander(operation, modifier, modifierValue):
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

    @staticmethod
    def importFigure(fileLocation):
        MeshWrapper.SingleInstanceApiCommander("open",fileLocation,None)

    @staticmethod
    def selectAll(): 
      Ui_WizardPage.SingleInstanceApiCommander("selectAll",None,None)

    @staticmethod
    def wireframe():
        print 'here'

    @staticmethod
    def remesh():
       MeshWrapper.SingleInstanceApiCommander("remesh","smooth",0.325)

    @staticmethod
    def deformsmooth():
       MeshWrapper.SingleInstanceApiCommander("smooth","scale",0.7)
     
    @staticmethod
    def roughtselectionforsocket():
        print 'here'
    
    @staticmethod
    def invertSelection():
        print 'here'

    @staticmethod
    def editoffset():
        Ui_WizardPage.SingleInstanceApiCommander("offset","distance",0.7)

    @staticmethod
    def ModifySmoothBoundary():
        Ui_WizardPage.SingleInstanceApiCommander("smoothboundary","smoothness",25.0)

    @staticmethod
    def editDiscard():
        Ui_WizardPage.SingleInstanceApiCommander("discard",None,None)

    @staticmethod
    def remeshsecondtime():
        Ui_WizardPage.SingleInstanceApiCommander("remesh","smooth",13)

    @staticmethod
    def selectleghide():
        print 'here'

    ## value changed events

    @staticmethod
    def remeshValueChanged(value):
       Ui_WizardPage.SingleInstanceApiCommander("remesh","smooth",value/float(100))

    @staticmethod
    def deformSmooth_smoothValueChanged(value):
        Ui_WizardPage.SingleInstanceApiCommander("smooth","scale",value/float(100))

    @staticmethod
    def offset_distanceValueChanged(value):
        print 'here'

    @staticmethod
    def smoothBoundary_distanceValueChanged(value):
        print 'here'

    @staticmethod
    def offsetSecond_distanceValueChanged(value):
        print 'here'

    @staticmethod
    def deformSmooth_scaleValueChanged(value):
        print 'here'

