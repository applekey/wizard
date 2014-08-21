import os,sys

def resource_path(relative):
    #if hasattr(sys, "_MEIPASS"):
    #    return os.path.join(sys._MEIPASS, relative)
    #else:
    #    return os.path.abspath(relative)
    #return os.path.join(relative)


    return os.path.abspath(relative)