import numpy as np
import numpy.linalg as linalg
import math as m


def calculateMax(origionalXValues,origionalYValues,origionalZValues,rotationMatrix):
    rX=[]
    rY=[]
    rZ=[]

    for i,x in enumerate(origionalXValues):
        coord = np.matrix([[x],[origionalYValues[i]],[origionalZValues[i]]])
        newcoord = rotationMatrix*coord
        x = newcoord.item((0,0))
        y = newcoord.item((1,0))
        z = newcoord.item((2,0))
       
        rX.append(x)
        rY.append(y)
        rZ.append(z)

    xMax = max(rX)
    yMax = max(rY)
    zMax = max(rZ)
    print xMax,yMax,zMax


def calculateRotationAngles(eigenVectors):
    print eigenVectors.item((2,0))
    zaxisrotation  = -m.asin(eigenVectors.item((2,0)))
    xaxisrotatfdsaion  = m.atan2(eigenVectors.item((2,1))/m.cos(zaxisrotation),eigenVectors.item((2,2))/m.cos(zaxisrotation))  
    zaxisrotateion = m.atan2(eigenVectors.item((1,0))/m.cos(zaxisrotation),eigenVectors.item((0,0))/m.cos(zaxisrotation))       
    return   zaxisrotation,  xaxisrotatfdsaion,   zaxisrotateion   

def calculateEigenVectors(filePath,downSampleCount): 

    xRow =[]
    yRow= []
    zRow = []

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
    #V = normalize(V,axis=0,norm='l2')
    V = linalg.inv(V)
    print '\n'
    print  V
    return xRow,yRow,zRow,V
    

#xRow,yRow,zRow,rotationVector = calculateEigenVectors("C:\\Users\\applekey\\Desktop\\daleg.obj",0)

#[r,phi,delta] =calculateRotationAngles(rotationVector)

#calculateMax(xRow,yRow,zRow,rotationVector)



#f = open("C:\\Users\\applekey\\Desktop\\output.obj",'w')

#for i,x in enumerate(xRow):
#    coord = np.matrix([[x],[yRow[i]],[zRow[i]]])
#    newcoord = vector*coord
#    x = newcoord.item((0,0))
#    y = newcoord.item((1,0))
#    z = newcoord.item((2,0))
#    f.write('v '+str(x)+' '+str(y)+' '+str(z)+'\n')
#    rX.append(x)
#    rY.append(y)
#    rZ.append(z)

#f.close()

## this creates the bounding box
#xMax = max(rX)
#yMax = max(rY)
#zMax = max(rZ)

#print xMax,yMax,zMax
   




