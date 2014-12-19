def tr(a):
    sum = 0
    for i in range(a.stride):
        sum = sum+ a[i,i]
    return sum

#def eigenVal(matrix):
#    pass
def dotp(a,b):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*b)] for X_row in a]
    print result
def addp(a,b):
    return map(lambda x,y:map(lambda w,z:w+z,x,y), a,b)

abc = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]


def bocher3x3(matrix):
    A2 = dotp(matrix,matrix)
    A3 = dotp(A2,matrix)
    trA = tr(matrix)
    trA2= tr(A2)
    trA2= tr(A3)
    a1 = -tr(matrix)
    a2 = -0.5*(dotp(a1,trA) + trA2)


#print gaussElimination(abc)

#print dotp(abc,abc)

print abc
print '\n'
print addp(abc,abc)