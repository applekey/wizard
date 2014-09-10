from MeshWrapper import *
from mmapi import  *

## use extensionFunction()

@meshWrapper
def selectTool():
    cmd  = mmapi.StoredCommands()
    cmd.AppendSelectCommand_All()
    cmd.AppendSelectUtilityCommand("invert") 
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
def complete():
    cmd  = mmapi.StoredCommands()
    cmd.AppendCompleteToolCommand('accept')
    return cmd

@meshWrapper
def separate():
    cmd  = mmapi.StoredCommands()
    cmd.AppendCompleteToolCommand('separate')
    return cmd

@meshWrapper
def separate():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('duplicate')
    return cmd

@meshWrapper
def offsetDistance(distance):
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('offset')
    cmd.AppendToolParameterCommand('offsetWorld',distance)
    cmd.AppendToolUtilityCommand('connected',True)
    return cmd




@meshWrapper
def attractBrush():
    cmd  = mmapi.StoredCommands()
    cmd.AppendBeginToolCommand('volumeBrush')
    cmd.AppendToolUtilityCommand('setPrimary','attract')
    return cmd







