def square_matrix_simple(matrix=[]):
    matrix_x = matrix.copy()
    for i in range(len(matrix)):
        matrix_x[i] = list(map(lambda x: x**2, matrix[i]))
    return (matrix_x)
