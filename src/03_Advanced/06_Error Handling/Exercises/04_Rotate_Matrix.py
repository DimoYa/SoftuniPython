class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for r in matrix:
        if len(r) != matrix_length:
            raise MatrixSizeError("The size of the matrix is not a perfect square")

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()


mtrx = []

while True:
    line = input().split()
    if not line:
        break
    for element in line:
        if not element.isdigit():
            raise MatrixContentError("The matrix must consist of only integers")
    mtrx.append([int(x) for x in line])

rotate_matrix(mtrx)
for row in mtrx:
    print(*row, sep=' ')
