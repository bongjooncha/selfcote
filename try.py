matrix = [[1, 1, 1], [2, 3, 1], [3, 1, 2]]

for col_idx in range(len(matrix[0])):
    col = [row[col_idx] for row in matrix]
    print(col)
