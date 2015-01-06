import math

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

def poly3Solver(a,b,c,d):
    q = (3.0*c- math.pow(b,2.0))/9.0 
    r = -27*d + b*(9*c-2*math.pow(b,2)) 
    discriminant = math.pow(q,3)+math.pow(r,2)
    s = r + math.sqrt(discriminant) 
    t = r - math.sqrt(discriminant) 
    term1 = math.sqrt(3.0)*((-t + s)/2) 
    r13= 2 * math.sqrt(q) 
    x1=(- term1 + r13*math.cos(math.pow(q,3)/3) ) 
    x2=(- term1 + r13*math.cos(math.pow(q,3)+(2*math.pi)/3) ) 
    x3=(- term1 + r13*math.cos(math.pow(q,3)+(4*math.pi)/3) )
    return x1,x2,x3


#print gaussElimination(abc)

#print dotp(abc,abc)

#print abc
#print '\n'
#print addp(abc,abc)
b,c,d= bocher3x3(abc)


import numpy as np
coeff = [1, b, c,d][::-1]
print np.roots(coeff)

print poly3Solver(1,b,c,d)