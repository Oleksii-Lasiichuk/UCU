"""Midterm"""
from copy import deepcopy

def read_checkerboard(path: str) -> list:
    """
    Reads a checkerboard configuration from a file and
    returns a list of lists representing the checkers on the board.

    The file at the given path should contain lines
    with comma-separated values representing
    the positions and states of checkers on the board.
    Each line corresponds to one square on
    the board, with the following format:
        column_label, row_number, square_color, checker_info

    Parameters:
    -----------
    path : str
        The file path to read the checkerboard configuration from.

    Returns:
    --------
    list[list[str]]:
        A list of lists where each inner list contains four elements:
        [column_label, row_number, square_color, checker_info]

    Example:
    --------
    >>> read_checkerboard('board.txt')
    [['a', '1', 'B', 'W'], ['b', '1', 'W', 'False'], ['c', '1', 'B', 'False'],\
 ['a', '2', 'W', 'False'], ['b', '2', 'B', 'B'], ['c', '2', 'W', 'W'],\
 ['a', '3', 'B', 'False'], ['b', '3', 'W', 'False'], ['c', '3', 'B', 'False']]
    """
    with open(path, "r", encoding='utf-8') as file:
        lines = file.read().splitlines()
        lst_lines = []
        for line in lines:
            line = line.split(",")
            lst_lines.append(line)
    return lst_lines


def decode_checkerboard(content: str) -> list:
    """
    Decodes the checkerboard information into a 2D list
    representing the board with checkers.

    Parameters:
    -----------
    content : list[list[str]]
        The checkerboard information as read from the file, where
        each inner list contains:
        [column_label, row_number, square_color, checker_info]

    Returns:
    --------
    list[list[tuple[str, str]]]:
        A 2D list representing the board, where each element is a tuple:
        (square_color, checker), where 'square_color' is 'b' or 'w',
        and 'checker' is 'w', 'b', or '' (empty string) for no checker.

    Example:
    --------
    >>> board = [['a', '1', 'B', 'W'], ['b', '1', 'W', 'False'], ['c', '1', 'B', 'False'],\
 ['a', '2', 'W', 'False'], ['b', '2', 'B', 'B'], ['c', '2', 'W', 'W'],\
 ['a', '3', 'B', 'False'], ['b', '3', 'W', 'False'], ['c', '3', 'B', 'False']]
    >>> decode_checkerboard(board)
    [[('b', 'w'), ('w', ''), ('b', '')], \
[('w', ''), ('b', 'b'), ('w', 'w')], \
[('b', ''), ('w', ''), ('b', '')]]
    """
    board = []
    counter = 0
    per_board = []
    for line in content:
        x = line[-2].lower()
        if line[-1] == "False":
            y = ''
        else:
            y = line[-1].lower()
        elements = (x, y)
        per_board.append(elements)
        counter += 1
        if counter == 3:
            board.append(per_board)
            per_board = []
            counter = 0
    return board

def remove_wrong_checkers(board: list, inplace=True) -> list | None:
    """
    Removes checkers that are placed on white squares,
    which is not allowed in the game of checkers.

    Parameters:
    -----------
    board : list[list[tuple[str, str]]]
        A 2D list representing the board, where each element is a tuple:
        (square_color, checker), with 'square_color' as 'b' or 'w',
        and 'checker' as 'w', 'b', or ''.

    inplace : bool, optional
        If True, modifies the input board in place and returns None.
        If False, returns a new board with the wrong checkers removed,
            leaving the input board unchanged.

    Returns:
    --------
    None or list[list[tuple[str, str]]]:
        If inplace is True, returns None after modifying the board in place.
        If inplace is False, returns a new board with checkers
            removed from white squares.
        If there were no wrong checkers to remove, returns None.

    Example:
    --------
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', 'w')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> remove_wrong_checkers(board)
    >>> board
    [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', '')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> remove_wrong_checkers(board) is None
    True
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', 'w')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> remove_wrong_checkers(board, inplace=False)
    [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', '')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> board
    [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', 'w')],\
 [('b', ''), ('w', ''), ('b', '')]]
    """
    new_board = deepcopy(board)
    output_board = []
    per_board = []
    counter = 0
    if inplace:
        for line in board:
            for el in line:
                if el[0] == "w":
                    elements = (el[0], "")
                    el = (elements)
                    counter += 1
                    if counter == 3:
                        output_board.append(per_board)
                        per_board = []
                        counter = 0
                else:
                    per_board.append(el)
                    counter += 1
                    if counter == 3:
                        output_board.append(per_board)
                        per_board = []
                        counter = 0
        board = deepcopy(output_board)
        return None
    else:
        for line in new_board:
            for el in line:
                if el[0] == "w":
                    elements = (el[0], "")
                    per_board.append(elements)
                    counter += 1
                    if counter == 3:
                        output_board.append(per_board)
                        per_board = []
                        counter = 0
                else:
                    per_board.append(el)
                    counter += 1
                    if counter == 3:
                        output_board.append(per_board)
                        per_board = []
                        counter = 0
        return output_board
            

def get_possible_captures_for_checker(board: list, position: tuple) -> list:
    """
    Checks all possible capture moves for a single checker at a given position.

    Parameters:
    -----------
    board : list[list[tuple[str, str]]]
        The game board.
    position : tuple[int, int]
        The (row_index, column_index) of the checker.

    Returns:
    --------
    list[tuple[tuple[int, int]]]:
        A list of possible capture moves for the checker at the given position.
        Each move is represented as:
        - ((start_row, start_col), (end_row, end_col)), (captured_row, captured_col))
        The list should be sorted by the (end_row, end_col) move. For example,
        if possible end moves are (5, 5), (1, 1), (1, 5), (5, 1) than the order should be
        corresponding to the following order:
        (1, 1), (1, 5), (5, 1), (5, 5)


    Example:
    --------
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', '')],\
 [('b', ''), ('w', ''), ('b', '')]]
    >>> get_possible_captures_for_checker(board, (0, 0))
    [((0, 0), (2, 2), (1, 1))]
    >>> get_possible_captures_for_checker(board, (1, 1))
    []
    >>> get_possible_captures_for_checker(board, (0, 1))
    []
    >>> board = [[('b', ''), ('w', ''), ('b', ''), ('w', ''), ('b', '')],\
 [('w', ''), ('b', 'b'), ('w', ''), ('b', ''), ('w', '')],\
 [('b', ''), ('w', ''), ('b', 'w'), ('w', ''), ('b', '')],\
 [('w', ''), ('b', ''), ('w', ''), ('b', 'b'), ('w', '')],\
 [('w', ''), ('b', ''), ('w', ''), ('b', ''), ('w', '')]]
    >>> get_possible_captures_for_checker(board, (2, 2))
    [((2, 2), (0, 0), (1, 1)), ((2, 2), (4, 4), (3, 3))]
    """
    ...

def write_board_to_file(board: list, pathname: str) -> None:
    """
    Writes the board to a file in a human-readable format.

    The board is represented as lines of squares, where each square
    is represented as:
    - |_| for a black empty square
    - | | for a white empty square
    - |w| or |b| for a square with a white or black checker

    Parameters:
    -----------
    board : list[list[tuple[str, str]]]
        A 2D list representing the board, where each element is a tuple:
        (square_color, checker), with 'square_color' as 'b' or 'w',
        and 'checker' as 'w', 'b', or ''.

    pathname : str
        The file path to write the board to.

    Returns:
    --------
    None

    Example:
    --------
    >>> board = [[('b', 'w'), ('w', ''), ('b', '')], \
[('w', ''), ('b', 'b'), ('w', 'w')], \
[('b', ''), ('w', ''), ('b', '')]]
    >>> write_board_to_file(board, 'result.txt')
    >>> with open('result.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    |w| |_|
    | |b|w|
    |_| |_|
    >>> board = [[('b', ''), ('w', ''), ('b', '')],\
 [('w', ''), ('b', ''), ('w', '')],\
 [('b', ''), ('w', ''), ('b', 'w')]]
    >>> write_board_to_file(board, 'result.txt')
    >>> with open('result.txt', 'r', encoding='utf-8') as file:
    ...    print(file.read())
    |_| |_|
    | |_| |
    |_| |w|
    """
    ...


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
