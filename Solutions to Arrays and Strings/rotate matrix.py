def rotate(matrix):

    N=len(matrix)

    for layer in range(N//2):
        first , last = layer, N - layer - 1

        for i in range(first, last):

            top = matrix[layer][i]

            matrix[layer][i] = matrix[-i-1][layer]

            matrix[-i-1][layer] = matrix[-layer-1][-i-1]

            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

            matrix[i][-layer-1] = top
    

    #printing
    print("Result: ")
    display(matrix)


def transpose_reverse(matrix):

    """
    Here we first transpose the matrix as rotating by a 90 degreee angle itself is
    making the rows become columns. However, the rows when noticed get reversed, hence
    we need to reverse thr rows of our transposed matrix.
    When compared to the rotated matrix, out transposed and reversed rows matrix would
    be the same.
    """

    #transpose
    N=len(matrix)

    for i in range(N):
        for j in range(i+1,N):
            temp= matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp

    print("The Transposed Matrix is: ")
    display(matrix)

    # now reversing the rows of the matrix

    for i in range(N):
        matrix[i]=matrix[i][::-1]
    
    print("Result from transpose and reverse: ")
    display(matrix)





def display(matrix):

    #displays the matrix

    N=len(matrix)

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()





matrix0=[[1]]
matrix1=[[1,2],[3,4]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
matrix3=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

transpose_reverse(matrix0)
transpose_reverse(matrix1)
transpose_reverse(matrix2)
transpose_reverse(matrix3)
print("+++++++++++++++++++++++++++++")

rotate(matrix0)
rotate(matrix1)
rotate(matrix2)
rotate(matrix3)