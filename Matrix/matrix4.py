def printmatrix(matrix):
    r,c = len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()

def transpose(matrix):
    matrix = [[1,4],[2,5],[3,6]]
    r,c = len(matrix),len(matrix[0])
    t_matrix = [[matrix[j][i] for j in range(r)] for i in range(c)]
    printmatrix(t_matrix)

def transposesquarematrix(matrix):
    matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    printmatrix(matrix)
