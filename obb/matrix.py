def tr(a):
    sum = 0
    for i in range(len(a)):
        sum = sum+ a[i][i]
    return sum

#def eigenVal(matrix):
#    pass
def dotp(a,b):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*b)] for X_row in a]
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
    trA3= tr(A3)
    a1 = -tr(matrix)
    a2 = -0.5*(a1*trA)
    a3 = -1/3*(a2*trA+a1*trA2+trA3)
    return a1,a2,a3

#print gaussElimination(abc)

#print dotp(abc,abc)

#print abc
#print '\n'
#print addp(abc,abc)
print bocher3x3(abc)