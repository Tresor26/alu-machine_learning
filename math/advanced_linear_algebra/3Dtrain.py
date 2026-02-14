A = [[2, 1, 3], 
     [4, 0, 5], 
     [6, 7, 8]]

def matrix(A):
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]

    det = a * (e*i - f*h) - b * (d*i - f*g) + c * (d*h - e*g)

    c11, c12, c13 = (e*i - f*h), (d*i - f*g), (d*h - e*g)
    c21, c22, c23 = (b*i - c*h), (a*i - c*g), (a*h - b*g)
    c31, c32, c33 = (b*f - c*e), (a*f - c*d), (a*e - b*d)

    minor = [[c11, c12, c13], 
             [c21, c22, c23], 
             [c31, c32, c33]]
    cof = [[c11, -c12, c13], 
            [-c21, c22, -c23], 
            [c31, -c32, c33]]
    
    adj = [[cof[0][0], cof[1][0], cof[2][0]], 
           [cof[0][1], cof[1][1], cof[2][1]], 
           [cof[0][2], cof[1][2], cof[2][2]]]
    
    inv = [[val / det for val in row] for row in adj]

    return det, minor, cof, adj, inv


determinant, minor, cofactor, adjugate, inverse = matrix(A)

print(f"Determinant:\n{determinant}\n")
print(f"Minor Matrix:\n{minor}\n")
print(f"Cofactor Matrix:\n{cofactor}\n")
print(f"Adjugate Matrix:\n{adjugate}\n")
print(f"Inverse Matrix:\n{inverse}\n")