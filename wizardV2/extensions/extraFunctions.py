from MeshWrapper import *
from mmapi import  *

## use extensionFunction()
def importFile():
    MeshWrapper.importFile()
def planeCut():
    return MeshWrapper.planecut()

@meshWrapper
def createFaceGroup():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('createFaceGroup') 
    return cmd

@meshWrapper
def selectTool():
    cmd  = mmapi.StoredCommands()
    cmd.AppendSelectCommand_All()
    cmd.AppendSelectUtilityCommand("invert") 
    return cmd

@meshWrapper
def repairAll():
    cmd  = mmapi.StoredCommands()
    cmd.AppendToolUtilityCommand("repairAll")
    return cmd

@meshWrapper
def inspector():
    cmd  = mmapi.StoredCommands()
    cmd.AppendCompleteToolCommand("cancel") 
    cmd.AppendBeginToolCommand('inspector') 
    return cmd

@meshWrapper
def selectAll():
    cmd  = mmapi.StoredCommands()
    cmd.AppendSelectCommand_All()
    return cmd

@meshWrapper
def discard():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('discard') 
    return cmd

@meshWrapper
def invertTool():
    cmd  = mmapi.StoredCommands()
    cmd.AppendSelectUtilityCommand("invert") 
    return cmd

@meshWrapper
def expandToConnected():
    cmd  = mmapi.StoredCommands()
    cmd.AppendSelectCommand_All()
    cmd.AppendSelectUtilityCommand("expandToConnected") 
    return cmd



@meshWrapper
def cancel():
    cmd  = mmapi.StoredCommands()
    cmd.AppendCompleteToolCommand("cancel") 
    return cmd

@meshWrapper
def fitPrimitive():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('fitPrimitive') 
    return cmd


@meshWrapper
def smoothBoundary():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('smoothBoundary') 
    return cmd

@meshWrapper
def accept():
    cmd  = mmapi.StoredCommands()
    cmd.AppendCompleteToolCommand('accept')
    return cmd

@meshWrapper
def separate():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('separate')
    return cmd


@meshWrapper
def offsetDistance(distance,checked=False):
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('offset')
    cmd.AppendToolParameterCommand('offsetWorld',distance)
    if checked:
        cmd.AppendToolUtilityCommand('connected',True)
    return cmd

@meshWrapper
def connected(state):
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('offset')
    cmd.AppendToolParameterCommand('Connected',state)
    return cmd

@meshWrapper
def offsetSmooth(value):
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('offset')
    cmd.AppendToolParameterCommand('softTransition',value)
    return cmd





@meshWrapper
def attractBrush():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('volumeBrush')
    cmd.AppendToolUtilityCommand('setPrimary','attract')
    return cmd

@meshWrapper
def colorView():
    cmd  = mmapi.StoredCommands()
    cmd.ViewControl_SetTriangleColorMode(1)
    
    return cmd

@meshWrapper
def align():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('align')
    
    return cmd



@meshWrapper
def alignZCam():
    cmd  = mmapi.StoredCommands()

    eye = vec3f()
    eye.x = -10.0
    eye.y= 0
    eye.z = 0

    target = vec3f()
    target.x = 0.0
    target.y= 0
    target.z = 0

    up = vec3f()
    up.x = 0.0
    up.y= 1.0
    up.z = 0.0
    
  
    cmd.CameraControl_SetSpecificView(eye,target,up)
    return cmd


## fileIOFunction()

def saveStep(stepArray):
    step = 'wizTmp'
    for s in stepArray:
        step = step+ '_'+str(s)
    step = step + '.mix'
    saveLatest(step)

   
def loadStep(stepArray):
    step = 'wizTmp'
    for step in stepArray:
        step = step+ '_'+str(step)
    step = step + '.mix'
    loadLatest(step)

@meshWrapper
def loadLatest(self,name):
    cmd  = mmapi.StoredCommands()
    currentDir = os.getcwd()
    saveFile = currentDir+name
    if os.path.isfile(saveFile):
        cmd.AppendSceneCommand_OpenMixFile(saveFile)
    return cmd

@meshWrapper
def saveLatest(self,name):
    cmd  = mmapi.StoredCommands()
    currentDir = os.getcwd()
    saveFile = currentDir+name
    cmd.AppendSceneCommand_ExportMixFile(saveFile)
    return cmd


