A=[[2, 3], 
   [1, 4]]

def matrix(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

print(matrix(A))