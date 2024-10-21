""" Target_en"""
import random
from copy import deepcopy

def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', \
'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    vowels = ['A', 'E', 'I', 'O', 'U']
    grid = []
    for _ in range(2):
        grid.append(random.choices(consonants, k=3))
    grid.append(random.choices(vowels, k=3))
    return grid


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f,"r", encoding="utf-8") as file:
        words = [line.strip() for line in file.readlines()]

    letters = [letter.lower() for letter in letters]

    correct_words = []
    for word in words:
        current_letters = deepcopy(letters)
        word_str = list(word.lower())
        counter = 0
        for char in word.lower():
            if char in current_letters:
                counter += 1
                current_letters.remove(char)
        if counter == len(word) and letters[4] in word_str and len(word) > 3:
            correct_words.append(word.lower())

    return correct_words

def get_user_words() -> list[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    words = []
    word=""
    try:
        while word != "end":
            word = input("Please suggest your words here: ")
            words.append(word)
        return words
    except EOFError:
        return words

def get_pure_user_words(user_words: list[str], letters: list[str], \
words_from_dict: list[str]) -> list[str]:
    """
    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    letters = [letter.lower() for letter in letters]

    correct_words = []
    for word in user_words:
        current_letters = deepcopy(letters)
        word_str = list(word.lower())
        counter = 0
        for char in word.lower():
            if char in current_letters:
                counter += 1
                current_letters.remove(char)
        if counter == len(word) and \
        letters[4] in word_str and len(word) > 3 \
        and word not in words_from_dict:
            correct_words.append(word.lower())
    return correct_words


def main():
    """
    The final combination of all func
    """
    grid = generate_grid()
    letters = [el for line in grid for el in line]
    dict_words = get_words("en.txt", letters)

    print("Your board is: ", grid)
    user_words = get_user_words()

    right_words = [i for i in user_words if i in dict_words]
    print(f"Number of the right words is: {len(right_words)}")
    print(f"All possible words: \n{dict_words}")

    missed_words = [i for i in dict_words if i not in user_words]
    print(f"You missed the following words: \n{missed_words}")

    incorect_words = get_pure_user_words(user_words, letters, dict_words)
    return f"You suggest, but we don't have them in the dictionary: \n{incorect_words}"

if __name__ == '__main__':
    # print(main())
    n = get_words("en.txt", ['v','h','t','d','s','r','a','e','l'])
    print(get_pure_user_words(['seva', 'seht', 'sera', 'sare', 'ltr', 'qrt', 'g', 'wwwww', 'rtgf', 'sxdl', 'sedl', 'tsal'],['v','h','t','d','s','r','a','e','l'], [n]))
