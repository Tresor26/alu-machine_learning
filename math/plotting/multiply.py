matrix_1 = [[1, 0],
            [0, 1]]

matrix_2 = [[3, 4],
            [9, 8]]


results = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            results[i][j] += matrix_1[i][k] * matrix_2[k][j]
    
print(results)
