def get_matrix(n, m, value):
    matrix = []
    for i in range(1, n + 1):
        columns = []
        matrix.append(columns)
        for j in range (1, m + 1):
            columns.append(value)
    return matrix
result1 = get_matrix(3, 5, 78)
result2 = get_matrix(4, 7, 2)
result3 = get_matrix(2, 8, 111)
print(result1)
print(result2)
print(result3)