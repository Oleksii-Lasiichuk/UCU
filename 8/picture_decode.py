"""Picture decode HW"""
type Symbols = dict[str, list[tuple[int, int]]]

def read_file(path: str) -> Symbols:
    """
    Reads file and return dict where keys are symbols and values are coordinates

    :param path: (str): filepath

    :return: Symbols: dict where keys are symbols and values are coordinates
    """
    symbols = {}
    with open(path, encoding='utf-8') as file:
        lines = file.readlines()
        last_symb = ''
        for row in lines:
            if len(row) == 2:
                last_symb = row[0]
                symbols[last_symb] = []
            elif len(row) > 2:
                row = row.strip()
                row = row.split()
                # row = row.split('_')
                symbols[last_symb] = [(int(el.split('_')[0]), int(el.split('_')[1])) for el in row]
    return symbols

def save_pict_to_file(symbols: Symbols, textfile: str) -> None:
    """
    Func draws a picture of symbols from their coordinates

    :param symbols: Symbols: dict where keys are symbols and values are coordinates
    :param textfile: (str): path to file
    """
    height, width = 0, 0
    for coordinates in symbols.values():
        for coord in coordinates:
            height = max(coord[0], height)
            width = max(coord[1], width)
    grid = [[' ' for _ in range(width + 1)] for _ in range(height + 1)]

    for key, coordinates in symbols.items():
        for coord in coordinates:
            grid[coord[0]][coord[1]] = key
    with open(textfile, 'w', encoding='utf-8') as file:
        for line in grid:
            file.write(''.join(line) + '\n')

if __name__ == "__main__":
    import doctest
    n = read_file('picture.txt')
    save_pict_to_file(n, 'final_img.txt')
         