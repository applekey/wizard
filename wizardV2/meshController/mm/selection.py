import mmapi;
from convert import *;
from tool import *;


def clear_face_selection(remote):
    """clear current selection (if there is one) and exit selection tool"""
    cancel_tool(remote)

def select_all(remote):
    """select all faces (will begin selection tool if not in it)"""
    cmd = mmapi.StoredCommands()
    cmd.AppendCompleteToolCommand("cancel")
    cmd.AppendBeginToolCommand("select")
    cmd.AppendSelectCommand_All()
    remote.runCommand(cmd)


def selection_utility_command(remote, command_name):
    """run selection utility command"""
    cmd = mmapi.StoredCommands()
    cmd.AppendSelectUtilityCommand( command_name )
    remote.runCommand(cmd)



def list_selected_facegroups(remote):
    cmd = mmapi.StoredCommands()
    k = cmd.AppendSelectCommand_ListSelectedFaceGroups()
    remote.runCommand(cmd)
    vgroups = mmapi.vectori();
    cmd.GetSelectCommandResult_ListSelectedFaceGroups(k, vgroups)
    return vectori_to_list(vgroups)


def select_facegroups(remote, groups_list):
    """select facegroups"""
    cmd = mmapi.StoredCommands()
    vgroups = mmapi.vectori();
    for group in groups_list:
        vgroups.push_back(group);
    cmd2 = mmapi.StoredCommands()
    cmd2.AppendSelectCommand_ByFaceGroups(vgroups)
    remote.runCommand(cmd2)



def select_hit_triangle(remote, ray_origin, ray_direction):
    cmd = mmapi.StoredCommands()
    key = cmd.AppendSelectCommand_FirstTriangleIntersectingRay(ray_origin[0], ray_origin[1], ray_origin[2], ray_direction[0], ray_direction[1], ray_direction[2])
    remote.runCommand(cmd)


    