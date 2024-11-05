"""HW"""
def dict_reader_tuple(file_dict: str) -> list:
    """ 
    Reads a pronunciation dictionary file and returns a list of tuples.

    Each line in the file represents a word, its primary pronunciation variant, 
    and its phonemes. The function parses this data into a list of tuples, 
    where each tuple contains the word (str), variant (int), and a list of phonemes (list[str]).

    Parameters:
    -----------
    file_dict : str
        The path to the pronunciation dictionary file.

    Returns:
    --------
    list[tuple[str, int, list[str]]]:
        A list of tuples where each tuple contains a word, variant number, and phonemes.

    Example:
    --------
    >>> len(dict_reader_tuple('cmudict.txt'))
    133737
    >>> dict_reader_tuple('cmudict.txt')[4]
    ('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1'])
    """
    output = []
    with open(file_dict, encoding='utf-8') as file:
        lines = [line.strip().split() for line in file]
        output = [(word, int(number), args) for word, number, *args in lines]
    return output


def dict_reader_dict(file_dict: str) -> dict:
    """ 
    Reads a pronunciation dictionary file and returns a dictionary.

    Each word is a key in the dictionary, and the associated value is a set of tuples 
    containing possible phoneme sequences. If a word has multiple pronunciations, 
    they are stored as separate tuples within the set.

    Parameters:
    -----------
    file_dict : str
        The path to the pronunciation dictionary file.

    Returns:
    --------
    dict[str, set[tuple[str]]]:
        A dictionary where each key is a word, and the value is a set of phoneme tuples.

    Example:
    --------
    >>> len(dict_reader_dict('cmudict.txt'))
    123455
    >>> dict_reader_dict('cmudict.txt')['NACHOS'] =\
= {('N', 'AA1', 'CH', 'OW0', 'Z'), ('N', 'AE1', 'CH', 'OW0', 'Z')}
    True
    """
    output = {}
    with open(file_dict, encoding='utf-8') as file:
        lines = [line.strip().split() for line in file]
        for word, *args in lines:
            variant = tuple(args[1:])
            if word not in output:
                output[word] = {variant}
            else:
                output[word].add(variant)
    return output


def dict_invert(dct) -> dict:
    """ 
    Inverts a dictionary or list representation of a pronunciation dictionary.

    This function inverts the input structure by organizing words according 
    to the number of pronunciation variants they have. The input can be either 
    a list of tuples (from `dict_reader_tuple`) or a dictionary (from `dict_reader_dict`).

    Parameters:
    -----------
    dct : dict or list
        The pronunciation dictionary in dictionary or list format.

    Returns:
    --------
    dict[int, set[tuple[str, tuple[str]]]]:
        A dictionary where each key is the number of pronunciation variants, 
        and the value is a set of tuples with the word and phoneme sequence.

    Example:
    --------
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    >>> dict_invert([('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1'])])
    {1: {('AAA', ('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1'))}}
    >>> dict_invert({'AABERG': {('AA1', 'B', 'ER0', 'G')}, 'A.': {('EY1',)}, \
    'A': {('EY1',), ('AH0',)}, 'A42128': {('EY1', 'F', 'AO1', \
    'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T')}, \
    'AAA': {('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')}}) == \
    {1: {('A.', ('EY1',)), ('AABERG', ('AA1', 'B', 'ER0', 'G')), \
    ('AAA', ('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')), \
    ('A42128', ('EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T'))}, \
    2: {('A', ('EY1',)), ('A', ('AH0',))}}
    True
    >>> dict_invert(dict_reader_tuple('cmudict.txt')) =\
= dict_invert(dict_reader_dict('cmudict.txt'))
    True
    """
    output = {}
    if isinstance(dct, dict):
        for word, variants in dct.items():
            num = len(variants)
            if num not in output:
                output[num] = set()
            for variant in variants:
                output[num].add((word, tuple(variant)))
    if isinstance(dct, list):
        for word, num, variant in dct:
            if num not in output:
                output[num] = set()
            output[num].add((word, tuple(variant)))

    return output

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
