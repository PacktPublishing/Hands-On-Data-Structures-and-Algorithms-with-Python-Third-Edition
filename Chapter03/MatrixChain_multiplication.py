import sys
def MatrixChain(mat, i, j):
    if i == j: 
        return 0
    minimum_computations = sys.maxsize
    for k in range(i, j):
        count = (MatrixChain(mat, i, k) + MatrixChain(mat, k+1, j)+ mat[i-1] * mat[k] * mat[j])
    if count < minimum_computations:    
        minimum_computations = count   
    return minimum_computations  


matrix_sizes = [20, 30, 45, 50]  
print("Minimum multiplications are", MatrixChain(matrix_sizes , 1, len(matrix_sizes)-1))  
