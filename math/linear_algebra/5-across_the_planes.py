def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        if len(mat1[i]) != len(mat2[i]):
            return None
        new_matrix.append([mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))])
    return new_matrix