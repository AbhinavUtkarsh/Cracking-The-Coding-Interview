import numpy as np

def zero(matrix):

    """
    here we just store the location of 0s in the matrix
    in an array and take a second pass to make those 
    rows or columns 0
    """
    row=[]
    column=[]
    M=len(matrix)
    N=len(matrix[0])
    # reading the matrix
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==0:
                row.append(i)
                column.append(j)

    # using our array of rows and cols to make the matrix 0

    for i in range(M):
        for j in range(N):
            if (i in row) or (j in column):
                matrix[i][j]=0

    print("Result: ")
    display(matrix)

def zero_noarray(matrix):

    #note: this method needs to access columns of the matrix which we can't do with python lists without zip, using numpy is an option
    #however it seems to not work for me

    """
    here we will use the first row and col of the same matrix as our mapper to store 0s
    and in our second iteration we will just make those mapped locations 0
    """

    M=len(matrix)
    N=len(matrix[0])

    zeroInFirstRow=False
    zeroInFirstCol=False

    # checking zero for the first row

    for j in range(N):
        if matrix[0][j]==0:
            zeroInFirstRow=True
    
    # checking zero for the first col
    for i in range(M):
        if transpose(matrix)[i][0]==0:
            zeroInFirstCol=True
    
    # now checking other rows and cols to create the markers

    for i in range(1,M):
        for j in range(1,N):
            if matrix[i][j]==0:
                matrix[0][j]=0
                matrix[i][0]=0
    
    # zeroing the matrix based on rows

    for i in range(1,M):
        if matrix[i][0]==0:
            matrix[i]=[0]*N

    # zeroing the matrix based on cols

    for j in range(1,N):
        if matrix[0][j]==0:
            set_col(matrix,j)

    # if the first row had 0
    if zeroInFirstRow:
        matrix[0]=[0]*N
    
    #if the first col had 0
    
    if zeroInFirstCol:
        set_col(matrix,0)

    print("Results with no extra space (considering transpose as 0 extra space): ")

    display(matrix)





def set_col(matrix,j):

    # setting the col to zero
    matrix=list(transpose(matrix))
    matrix[j]=[0]*len(matrix[0])
    matrix=transpose(matrix)
    return matrix



def transpose(matrix):

    # transposes the matrix to allow python to iterate over cols
    copy=np.array(matrix)
    copy=np.transpose(copy)

    # although not needed as the parameters are pass by reference
    return copy.tolist()




def display(matrix):

    #displays the matrix

    M=len(matrix)

    N=len(matrix[0])
    for i in range(M):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()


matrix0=[[0]]
matrix1=[[1,0]]
matrix2=[[1,2],[4,5],[0,8]]
matrix3=[[9,876,11,0],[13,99,15,16]]

zero(matrix0)
zero(matrix1)
zero(matrix2)
zero(matrix3)

print("+++++++++++++++++++++++++++++")

matrix0=[[0]]
matrix1=[[1,0]]
matrix2=[[1,2],[4,5],[0,8]]
matrix3=[[9,876,11,0],[13,99,15,16]]

zero_noarray(matrix0)
#zero_noarray(matrix1)
#zero_noarray(matrix2)
#zero_noarray(matrix3)




