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
    with open("laba_dyscr/new_file.csv", "w", encoding="utf-8") as write_f:
        for _, line in enumerate(content):
            for i, el in enumerate(line):
                if i == len(line)-1:
                    write_f.write(el + "\n")
                else:
                    write_f.write(el)


def find_reflecsive(content: list) -> list:
    """
    func finds рефлексивне замикання if not found then makes it to be рефлексивне -_-
    """
    
    reflecsive_el = 0
    lenght = (len(content[0]) + 1) / 2 #враховуємо к-ть пробілів
    for _, line in enumerate(content):
        if line[reflecsive_el].isdigit():
            if int(line[reflecsive_el]) == 1:
                reflecsive_el += 2

    if reflecsive_el == lenght * 2:
        return content
    else:
        reflecsive = []
        counter = 0
        for _, line in enumerate(content):
            elements = line.split()
            elements[counter] = "1"
            reflecsive.append(" ".join(elements))
            counter += 1
        return reflecsive


def find_symmetric(content: list) -> list:
    """
    function makes symmetric zamukannia if needed
    """
    anti_content = [] #list content but here elements in the list are rows of n*n 
    len_of_line = len(content[0])
    num_of_lines = int((len_of_line+1)/2)

    elem_in_line = 0
    for _ in range(num_of_lines):
        column = ''
        for i, line in enumerate(content):
            column += line[elem_in_line]
            if i != num_of_lines-1:
                column += " "
        anti_content.append(column)
        elem_in_line += 2

    symetric = []
    #перевіряємо чи є вже дане відношення симетричним
    if anti_content == content:
        return content

    # порівнюємо через "побітове або" значення в рядку і колонці
    # (відношення симетричне якщо є 1,2 і є 2,1)
    for idx, line in enumerate(content):
        new_line = ''
        for i, el in enumerate(line):
            if el.isdigit():
                new_line += str(int(el) | int(anti_content[idx][i]))
            else:
                new_line += el
        symetric.append(new_line)
    return symetric


n = read_file('laba_dyscr/txtfile.csv')
write_in_file(find_symmetric(find_reflecsive(n)))
