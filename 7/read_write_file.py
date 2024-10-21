"""hw"""
from urllib.request import urlopen

def read_input_file(url: str, number: int) -> list[list[str]]:
    """
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url

    >>> read_input_file('https://rb.gy/97llc',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://rb.gy/97llc',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], \
['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    with urlopen(url) as f:
        readed = f.read().decode('utf-8').splitlines()
        lenght = len(readed)
        lines = []
        for i in range(lenght):
            if readed[i][0].isnumeric():
                lines.append(readed[i])
            elif readed[i][:2] == " С":
                lines.append(readed[i])
        all_info = []
        counter = 0
        for i in range(2, len(lines)+1, 2):
            all_info.append(lines[counter:i])
            counter += 2

        final_list = []
        one_person_info = []
        for person in all_info:
            one_person_info = []
            one_person_info = person[0].split("\t")[:4]
            one_person_info[2] = "+"
            one_person_info.append(person[1].split()[-1])
            final_list.append([i for i in one_person_info])
        output = []
        for i in range(number):
            output.append(final_list[i])
        return output

def write_csv_file(url: str):
    '''
    write info to csv file with the path total.csv
    
    >>> write_csv_file('https://rb.gy/97llc')
    >>> with open('total.csv', "r") as f:
    ...     print(f.readline(), end = "")
    ...     print(f.readline(), end = "")
    №,ПІБ,Д,Заг.бал,С.б.док.осв.
    1,Мацюк М. І.,+,197.859,10.80
    '''
    persons = read_input_file(url, 77)

    with open('total.csv', "w") as f:
        f.write("№,ПІБ,Д,Заг.бал,С.б.док.осв." + "\n")
        for person in persons:
            result = ",".join(person)
            f.write(result + '\n')

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
