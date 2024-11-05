def is_transitive(matrix: list[list])-> bool:
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[i][k] == 0:
                        return False
    return True

n = 5
lenght = n**2
number = '1' * lenght
number = int(number, 2)
counter = 0

for i in range(0, number+1):
    generated_num = f"{str(bin(i)[2:]):0>{lenght}}"
    generated_num = [int(el) for el in generated_num]

    new_matrix = []
    for i in range(n):
        new_matrix.append(generated_num[i * n:i * n + n])

    if is_transitive(new_matrix):
        counter += 1
print(counter)

