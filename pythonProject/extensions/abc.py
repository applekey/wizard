from MeshWrapper import *
from mmapi import  *

controller = MeshWrapper()
@meshWrapper
def ok22(abc):
    print abc
    cmd  = mmapi.StoredCommands()
    cmd.AppendSelectCommand_All()
    return cmd