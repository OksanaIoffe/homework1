print("вариант 5")
print("задание 1")
n = int(input())
A = []
for i in range(n):
    B = []
    for i in range(n):
        B.append(int(input()))
    A.append(B)

for i in range(n):
    for j in range(n):
        print(A[i][j], end = ' ')
    print()
C = [sorted(row) for row in A]
print(C)

print("задание 2")
def replace_elements(matrix):
    for row in matrix:
        min_val = min(row)
        index = row.index(min_val)
        if min_val % 2 == 0:
            row[index] = 0
        else:
            row[index] = 1
    return matrix


matrix = [[3, 7, 5],
          [2, 4, 6],
          [1, 9, 8]]
new_matrix = replace_elements(matrix)
for row in new_matrix:
    print(row)
