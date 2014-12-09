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

    a= np.cov(a)
    print a
    print '\n'

    L, V = linalg.eig(a)
    #V = normalize(V,axis=0,norm='l2')
    V = np.fliplr(V)
    V = linalg.inv(V)
    print linalg.det(V)
    angle = m.pi/2
    yRotation = np.matrix([[m.cos(angle), 0,-m.sin(angle)], [0, 1.0,0],[m.sin(angle), 0.0,m.cos(angle)]])
    xRotation =np.matrix([[1.0, 0,0], [0, m.cos(angle),-m.sin(angle)],[0, m.sin(angle),m.cos(angle)]])
    zRotation =np.matrix([[m.cos(angle), -m.sin(angle),0], [m.sin(angle), m.cos(angle),0],[0, 0,1]]) 
    V = np.dot(zRotation,V)
    print 'ofk'

    print L 
    print V
    return V
    

vector = calculateEigenVectors("daleg.obj",0)


f = open("output.obj",'w')

for i,x in enumerate(xRow):
    coord = np.matrix([[x],[yRow[i]],[zRow[i]]])
    newcoord = vector*coord
    f.write('v '+str(newcoord.item((0,0)))+' '+str(newcoord.item((1,0)))+' '+str(newcoord.item((2,0)))+'\n')


f.close()

   
