import mmapi;
from convert import *;
from tool import *;


def clear_face_selection(remote):
    """clear current selection (if there is one) and exit selection tool"""
    cancel_tool(remote)

