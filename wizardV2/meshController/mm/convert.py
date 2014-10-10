
def vectori_to_list(vi):
    sz = vi.size()
    lst = []
    for i in xrange(0,sz):
        lst.append( vi[i] )
    return lst

def vectorub_to_string(vub):
    sz = vub.size()
    lst = []
    for i in xrange(0,sz-1):    # skip trailing null
        lst.append( vub[i] )
    return str(bytearray(lst));

        
