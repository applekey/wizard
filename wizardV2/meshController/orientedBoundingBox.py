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


def numpyRollColumn(matrix):
    newMatrix = np.array(matrix, copy=True)  
    numberOfColumns = len(newMatrix[0,:])
    
    tmp = np.copy(newMatrix[:,0])
    for column in range(numberOfColumns-1):
        newMatrix[:,column] = newMatrix[:, column+1]
    newMatrix[:,numberOfColumns-1] = tmp
    return newMatrix


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
    orig = np.copy(V)
    solved =False
    if linalg.det(V) > 0:
        solved =True
    else:
        for ordering in range(2):
             V = numpyRollColumn(V)
             if linalg.det(V) > 0:
                 solved =True
                 break
        # reverse and do the same
        V = orig
        if solved == False:
            V = np.fliplr(V)
            if linalg.det(V) > 0:
                solved =True
            else:
                for ordering in range(3):
                        V = numpyRollColumn(V)
                        print V
                        print '\n'
                        if linalg.det(V) > 0:
                            solved =True
                            break
    if solved == False:
        raise Exception('i am bad')

    print linalg.det(V)


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
   




