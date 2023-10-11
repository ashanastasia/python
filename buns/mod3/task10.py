size = int(input("Введите размерность квадратной матрицы: "))

matrix = []
for i in range(1, size+1):
    row = list(range(1, size+1))
    matrix.append(row)

print("Исходная матрица:")
for row in matrix:
    print(", ".join(map(str, row)))

for i in range(size):
    for j in range(i+1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("\nТранспонированная матрица:")
for row in matrix:
    print(", ".join(map(str, row)))
