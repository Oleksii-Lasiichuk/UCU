"""HW"""
def read_file(file_path: str) -> list:
    """Reading file"""
    f_content = []
    counter = 1
    with open(file_path, 'r', encoding="utf-8") as read_f:
        for line in read_f:
            length = len(line)
            if counter * 2 - 1 == length:
                f_content.append(line[:length + 1])
            else:
                f_content.append(line[:length - 1])
            counter += 1
    return f_content

def write_in_file(content):
    """
    Write execution in new file
    """
    with open("new_file.csv", "w", encoding="utf-8") as write_f:
        for _, line in enumerate(content):
            for i, el in enumerate(line):
                if i == len(line)-1:
                    write_f.write(el + "\n")
                else:
                    write_f.write(el)

def find_columns(matrix_rows: list) -> list:
    """
    makes list of columns of matrix
    """
    matrix_rows = [i.replace(" ", "") for i in matrix_rows]
    matrix_columns = []
    len_of_line = len(matrix_rows[0])
    elem_in_line = 0
    for _ in range(len_of_line):
        column = ''
        for i, line in enumerate(matrix_rows):
            column += line[elem_in_line]
        matrix_columns.append(column)
        elem_in_line += 1
    return matrix_columns

def find_reflexive(matrix: list) -> list:
    """
    func finds рефлексивне замикання if not found then makes it to be рефлексивне -_-
    """

    reflecsive_el = 0
    lenght = (len(matrix[0]) + 1) / 2 #враховуємо к-ть пробілів
    for _, line in enumerate(matrix):
        if line[reflecsive_el].isdigit():
            if int(line[reflecsive_el]) == 1:
                reflecsive_el += 2

    if reflecsive_el == lenght * 2:
        return matrix
    else:
        reflecsive = []
        counter = 0
        for _, line in enumerate(matrix):
            elements = line.split()
            elements[counter] = "1"
            reflecsive.append(" ".join(elements))
            counter += 1
        return reflecsive

def find_symmetric(matrix_rows: list) -> list:
    """
    function makes symmetric zamukannia if needed
    """
    # makes another list of lists where each element is a column of matrix
    matrix_rows = [i.replace(" ", "") for i in matrix_rows]
    matrix_columns = find_columns(matrix_rows)

    symetric = []
    #перевіряємо чи є вже дане відношення симетричним
    if matrix_columns == matrix_rows:
        return matrix_rows

    # порівнюємо через "побітове або" значення в рядку і колонці
    # (відношення симетричне якщо є 1,2 і є 2,1)
    for idx, line in enumerate(matrix_rows):
        new_line = ''
        for i, el in enumerate(line):
            new_line += str(int(el) | int(matrix_columns[idx][i]))
            if i != len(matrix_rows[0])-1:
                new_line += " "
        symetric.append(new_line)
    return symetric

def find_transitive(matrix_rows: list) -> list:
    """
    makes транзитивне замикання
    """
    matrix_rows = [i.replace(" ", "") for i in matrix_rows]
    matrix_columns = find_columns(matrix_rows)

    lenght = len(matrix_rows[0])
    matrix = matrix_rows
    new_matrix = []
    for line in matrix:
        bulls = []
        for bull in line:
            bulls.append(bull)
        new_matrix.append(bulls)

    for c in range(lenght):
        matrix_rows = []
        for i in matrix:
            new_mat = ''
            for j in i:
                new_mat += j
            matrix_rows.append(new_mat)
        matrix_columns = find_columns(matrix_rows)


        position = []
        position_rows = []
        print(matrix_rows)
        print(matrix)
        for i, bull in enumerate(matrix_rows[c]):
            if bull == "1":
                position.append(int(i))
        position_rows.extend(position)

        position = []
        position_columns = []
        for i, bull in enumerate(matrix_columns[c]):
            if bull == "1":
                position.append(int(i))
        position_columns.extend(position)

        # splitting str, because str can not be changed
        # new_matrix = []
        # for line in matrix:
        #     bulls = []
        #     for bull in line:
        #         bulls.append(bull)
        #     new_matrix.append(bulls)

        for i in range(lenght):
            for x in position_columns:
                for y in position_rows:
                    new_matrix[x][y] = "1"
        matrix = new_matrix

    
    matrix = [" ".join(line) for line in matrix]
    print(matrix)
    return matrix

if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    n = read_file('incorect.csv')
    print(n)
    print(find_columns(n))
    # print(find_transitive(n))
