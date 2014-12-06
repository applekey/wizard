import numpy as np
import numpy.linalg as linalg
import math as m
from sklearn.preprocessing import normalize

xRow =[]
yRow= []
zRow = []
def calculateRotationAngles(eigenVectors):
    print eigenVectors.item((2,0))
    zaxisrotation  = -m.asin(eigenVectors.item((2,0)))
    xaxisrotatfdsaion  = m.atan2(eigenVectors.item((2,1))/m.cos(zaxisrotation),eigenVectors.item((2,2))/m.cos(zaxisrotation))  
    zaxisrotateion = m.atan2(eigenVectors.item((1,0))/m.cos(zaxisrotation),eigenVectors.item((0,0))/m.cos(zaxisrotation))       
    return   zaxisrotation,  xaxisrotatfdsaion,   zaxisrotateion   
def calculateEigenVectors(filePath,downSampleCount): 

    downsampleCount = downSampleCount

    f = open(filePath, 'r')
    count = 0
    for line in f:
        coordinates = line.split()
        if coordinates[0] == 'v':

   
            xRow.append(float(coordinates[1]))
            yRow.append(float(coordinates[2]))
            zRow.append(float(coordinates[3]))
            count = 0

    a = np.matrix([xRow,yRow,zRow])

    print a

    a= np.cov(a)


    print '\n'
    L, V = linalg.eig(a)
    print L

    print '\n'
    print  V
    V = normalize(V,axis=0,norm='l2')
    V = linalg.inv(V)
    print '\n'
    print  V
    return V
    

vector = calculateEigenVectors("test.obj",0)

[r,phi,delta] =calculateRotationAngles(vector)
print r,phi,delta
print m.degrees(r),m.degrees(phi),m.degrees(delta)

f = open("output.obj",'w')

for i,x in enumerate(xRow):
    coord = np.matrix([[x],[yRow[i]],[zRow[i]]])
    newcoord = vector*coord
    f.write('v '+str(newcoord.item((0,0)))+' '+str(newcoord.item((1,0)))+' '+str(newcoord.item((2,0)))+'\n')


f.close()

   
