"""
Discrete maths relations lab
"""
from copy import deepcopy
from typing import List

def read_file(filename: str) -> List[List[int]]:
    """
    str -> list[list]
    Reads matrix from with name {filename} file and transforms it into a list of lists
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w",delete=False) as tmp:
    ...     _=tmp.write('0, 0, 1\\n0, 1, 1\\n1, 1, 1')
    >>> read_file(tmp.name)
    [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    """
    matrix = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip().replace(" ", "")
            line = line.split(",")
            row = [int(element) for element in line]
            matrix.append(row)
    return matrix

def write_to_file(filename: str, relation: List[List[int]]) -> None:
    """
    List[List[int]], str -> None
    Creates a file with input from {matrix}
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w",delete=False) as tmp:
    ...     _=tmp.write('')
    >>> write_to_file(tmp.name, [[0, 1, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 1, 1, 1]])
    >>> with open(tmp.name,"r",encoding="utf-8") as file:
    ...     print(file.read())
    0, 1, 0, 0
    1, 1, 1, 1
    1, 0, 0, 0
    1, 1, 1, 1
    """
    with open(filename, "w", encoding="utf-8") as f:
        for i, row in enumerate(relation):
            row_str = ''
            for j, element in enumerate(row):
                if j != len(row)-1:
                    row_str += str(element) + ', '
                else:
                    row_str += str(element) + ' '
            if i != len(row)-1:
                f.write(row_str.strip() + '\n')
            else:
                f.write(row_str.strip())

def find_columns(matrix_rows: list) -> list:
    """
    makes list of columns of matrix
    """
    matrix_columns = []
    len_of_line = len(matrix_rows[0])
    for i in range(len_of_line):
        column = []
        for _, line in enumerate(matrix_rows):
            column.append(line[i])
        matrix_columns.append(column)
    return matrix_columns

def find_reflexive_closure(matrix: List[List[int]])-> List[List[int]]:
    """
    List[List[int]] -> List[List[int]]
    Finds reflective closure of {matrix}
    >>> find_reflexive_closure([[0, 0, 0, 0],[1, 0, 1, 1],[0, 0, 0, 0],[1, 1, 0, 0]])
    [[1, 0, 0, 0], [1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 0, 1]]
    """
    for index, line in enumerate(matrix):
        line[index] = 1
    return matrix

def find_symmetrical_closure(matrix_rows: List[List[int]])-> List[List[int]]:
    """
    List[List[int]] -> List[List[int]]
    Finds symmetrical closure of {matrix}
    >>> find_symmetrical_closure([[0, 1, 0, 0],[1, 1, 1, 1],[0, 0, 1, 0],[1, 1, 0, 1]])
    [[0, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1]]
    """
    matrix_columns = find_columns(matrix_rows)
    symetric = []

    #перевіряємо чи є вже дане відношення симетричним
    if matrix_columns == matrix_rows:
        return matrix_rows

    # порівнюємо через "побітове або" значення в рядку і колонці
    # (відношення симетричне якщо є 1,2 і є 2,1)
    for idx, line in enumerate(matrix_rows):
        new_line = []
        for i, el in enumerate(line):
            new_line.append(int(el) | int(matrix_columns[idx][i]))
        symetric.append(new_line)
    return symetric

def find_transitive_closure(matrix: List[List[int]])-> List[List[int]]:
    """
    List[List[int]] -> List[List[int]]
    Finds reflexive closure of {matrix}
    >>> find_transitive_closure([[0, 1, 0, 0],[1, 1, 1, 1],[0, 0, 1, 0],[1, 1, 0, 1]])
    [[1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 1]]
    """
    closure = deepcopy(matrix)
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if closure[i][j] == 1 or (closure[i][k] == 1 and closure[k][j] == 1):
                    closure[i][j] = 1
    return closure

def split_into_classes(matrix: List[List[int]])-> List[List[int]]:
    """
    List[List[int]] -> List[List[int]]
    Splits relation into equivalence classes
    >>> split_into_classes([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
    [[0, 1, 2], [3]]
    >>> split_into_classes([[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]])
    [[0, 1], [2, 3]]
    """
    classes = []
    lenght = len(matrix[0])
    for i in range(lenght):
        current_class = []
        for j in range(lenght):
            if matrix[i][j] == 1:
                current_class.append(j)
        if current_class not in classes:
            classes.append(current_class)
    return classes

def is_transitive(matrix: list[list])-> bool:
    """
    list[list] -> bool
    Check if given relation is transitive. Returns True if yes and False if no
    >>> is_transitive([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    >>> is_transitive([[0,1,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
    False
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                for k in range(n):
                    if matrix[j][k] == 1 and matrix[i][k] == 0:
                        return False
    return True

def find_transitive_number(n: int)-> int:
    """
    int -> int
    Return how many transitive relations are there on relation with n elements.
    (number<=4)
    >>> find_transitive_number(0)
    1
    >>> find_transitive_number(2)
    13
    >>> find_transitive_number(3)
    171
    """
    if n == 0:
        return 1
    number = int('1' * n**2, 2)
    counter = 0

    for i in range(0, number+1):
        generated_num = f"{str(bin(i)[2:]):0>{n**2}}"
        generated_num = [int(el) for el in generated_num]

        new_matrix = []
        for i in range(n):
            new_matrix.append(generated_num[i * n:i * n + n])

        if is_transitive(new_matrix):
            counter += 1
    return counter

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
