import numpy as np

def min_cost(matrix, i, j, source, target):
    del_cost = matrix[i-1][j] + 1
    ins_cost = matrix[i][j-1] + 1
    sub_cost = matrix[i-1][j-1] + (1 if source[j-1] != target[i-1] else 0)
    return min(del_cost, ins_cost, sub_cost)

def compute_Levenshtein_distance(source, target):
    M = len(source)+1
    N = len(target)+1
    matrix = np.zeros((N, M))

    matrix[0][0] = 0

    for i in range(M):
        matrix[0][i] = i
    
    for j in range(N):
        matrix[j][0] = j

    for i in range(1,N):
        for j in range(1,M):
            matrix[i][j] = min_cost(matrix, i, j, source, target)

    return matrix[N-1][M-1]
            

assert compute_Levenshtein_distance("hi", "hello") == 4.0
print(compute_Levenshtein_distance("hola", "hello") )