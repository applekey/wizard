class matrix():
    stride = 3
    def __init__(self,values):
        self.values = values
    def v(self,row,column):
        index = row*self.stride+column
        return self.values[index]
    def setv(self,row,column,value):
        index = row*self.stride+column
        self.values[index] = value

    def __str__(self):
        values = []
        index = 0
        for i in range(self.stride):
            values.append(self.values[index:index+self.stride])
            index = index + self.stride
        return str(values)
    def __getitem__(self, index):
        row = index[0]
        column = index[1]
        return self.v(row,column)
    def __setitem__(self,index,value):
        row = index[0]
        column = index[1]
        self.setv(row,column,value)

def gaussElimination(a):
    for i in range(a.stride-1):
        for j in range(a.stride):
            ratio = a[i,j]/a[i,i]
            for k in range(i,a.stride):
                a[j,k] -= (ratio*a[i,k]) 
                #b[j] -= (ratio*b[i])
    return a



    #for (int i = 0; i < N-1; i++) { 
    #    for (int j = i; j < N; j++) { 
    #        double ratio = A[j][i]/A[i][i]; 
    #        for (int k = i; k < N; k++) { 
    #            A[j][k] -= (ratio*A[i][k]); 
    #            b[j] -= (ratio*b[i]); 
    #        } 
    #    } 
    #}

#def eigenVal(matrix):
#    pass


abc = matrix([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
print gaussElimination(abc)
