"""HW"""
def read_file(file_path):
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
    """Write execution in new file"""
    with open("laba_dyscr/new_file.csv", "w", encoding="utf-8") as write_f:
        for _, line in enumerate(content):
            for i, el in enumerate(line):
                if i == len(line)-1:
                    write_f.write(el + "\n")
                else:
                    write_f.write(el)

def find_reflect(content):
    """finding рефлексивне замикання"""
    # for line in content:
    #     for el in line:
    #         if el == " ":
    #             el = el.replace(" ", "")
    # return content
    counter = 0
    lenght = (len(content[0]) + 1) / 2
    for _, line in enumerate(content):
        for bull in line:
            if bull.isdigit():
                if int(bull) == 1:
                    counter += 2
    if counter == lenght:
        return "is reflective"
    return "is not"


n = read_file('laba_dyscr/txtfile.csv')
print(n)
print(find_reflect(n))
