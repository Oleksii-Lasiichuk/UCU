""" Target UA"""
import random
from random import choice

def generate_grid() -> list[list[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    """
    all_letters = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж",\
"з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с",\
"т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]

    grid = []
    while len(grid) < 5:
        letter = choice(all_letters)
        if letter not in grid:
            grid.append(letter)
    return grid


def get_words(f: str, letters: list[str]) -> list[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words("base.lst", ['щ', 'и', "б", "в", "і"])
    [('багі', 'noun'), ('баґґі', 'noun'), ('баки', 'noun'), ('бані', 'noun'), ('баси', 'noun'), \
('баші', 'noun'), ('баяті', 'noun'), ('бгати', 'verb'), ('бебі', 'noun'), ('бенді', 'noun'), \
('бити', 'verb'), ('біб', 'noun'), ('бігти', 'verb'), ('білі', 'noun'), ('білі', 'noun'), \
('бісів', 'adjective'), ('богів', 'adjective'), ('бонги', 'noun'), ('борщ', 'noun'), \
('босі', 'noun'), \
('брати', 'verb'), ('брити', 'verb'), ('брі', 'noun'), ('броги', 'noun'), ('буки', 'noun'), \
('булів', 'adjective'), ('бурав', 'noun'), ('буфи', 'noun'), ('буяти', 'verb'), ('буяхи', 'noun'), \
('ваги', 'noun'), ('вамбі', 'noun'), ('вбити', 'verb'), ('вбути', 'verb'), ('вгав', 'noun'), \
('вглиб', 'adverb'), ('вгорі', 'adverb'), ('вдати', 'verb'), ('вдіти', 'verb'), ('вдути', 'verb'), \
('веб', 'noun'), ('везти', 'verb'), ('верхи', 'adverb'), ('вессі', 'noun'), ('вести', 'verb'), \
('вжити', 'verb'), ('взути', 'verb'), ('взяти', 'verb'), ('вийти', 'verb'), ('вилив', 'noun'), \
('вилки', 'noun'), ('вилов', 'noun'), ('виріб', 'noun'), ('вируб', 'noun'), ('висів', 'noun'), \
('вити', 'verb'), ('вити', 'verb'), ('вияв', 'noun'), ('відси', 'adverb'), ('вікі', 'noun'), \
('вірні', 'noun'), ('віскі', 'noun'), ('віші', 'noun'), ('віяти', 'verb'), ('вкупі', 'adverb'), \
('влити', 'verb'), ('влови', 'noun'), ('вмити', 'verb'), ('вміти', 'verb'), ('вночі', 'adverb'), \
('волхв', 'noun'), ('вплав', 'adverb'), ('вплив', 'noun'), ('врити', 'verb'), ('вроки', 'noun'), \
('вруб', 'noun'), ('всюди', 'adverb'), ('втяти', 'verb'), \
('вужів', 'adjective'), ('вчити', 'verb'), \
('вчути', 'verb'), ('вшити', 'verb'), ('івасі', 'noun'), ('ізнов', 'adverb'), ('ікати', 'verb'), \
('інкуб', 'noun'), ('іноді', 'adverb'), ('іти', 'verb'), ('щасні', 'noun'), ('щипці', 'noun'), \
('щі', 'noun'), ('щодві', 'adverb'), ('щотри', 'adverb')]
    """
    with open(f,"r", encoding="utf-8") as file:
        words = [line.strip() for line in file.readlines()]
    letters = [letter.lower() for letter in letters]

    correct_words = []
    temp = ['/n', 'adj', '/v', 'adv', 'noun', 'verb']
    for word in words:
        temp_str = word.split()
        if len(temp_str) <2:
            continue
        if len(temp_str[0]) > 5:
            continue
        if len(temp_str[0]) < 2:
            continue
        if temp_str[0][-1] not in letters or temp_str[0][0] not in letters:
            continue
        if temp[0] in temp_str[1] or temp[4] in temp_str[1] and temp_str != 'intj':
            correct_words.append((temp_str[0].lower(), "noun"))
        elif temp[1] in temp_str[1]:
            correct_words.append((temp_str[0].lower(), "adjective"))
        elif temp[2] in temp_str[1] or temp[5] in temp_str[1]:
            correct_words.append((temp_str[0].lower(), "verb"))
        elif temp[3] in temp_str[1]:
            correct_words.append((temp_str[0].lower(), "adverb"))
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
            word = input("")
            words.append(word)
        return words
    except (EOFError, KeyboardInterrupt):
        return words

def check_user_words(user_words: list, word_type: str, letters: list, path: str) -> tuple:
    """
    Checks correct user words and missed ones
    """
    correct_words = get_words(path, letters)
    correct_words = [word[0] for word in correct_words if word[1] == word_type]
    missed_words = []
    result = []
    for word in user_words:
        if word in correct_words:
            result.append(word)

    for word in correct_words:
        if not word in user_words:
            missed_words.append(word)
    return (result, missed_words)

def main():
    """
    The final combination of all func
    """
    print("Пограймо в гру!\n\nПридумай якомога більше слів, що мають не \
більше 5 літер\n та починаються і закінчуються на одну з наступних літер:")

    grid = generate_grid()
    print(" ", grid)

    parts = ['noun', 'verb', 'adjective', 'adverb']
    random.shuffle(parts)
    print("А ще ці слова мають бути наступною частиною мови:")
    print(" ", parts[0])

    print("Твій список слів: ")
    user_words = get_user_words()
    print(user_words)

    print("Правильно запропоновані слова: ", end="")
    print(check_user_words(user_words, parts[0], grid, "base_lst.lst"))

    correct_words = get_words("base_lst.lst", grid)
    correct_words = [word[0] for word in correct_words if word[1] == parts[0]]

    checked = get_user_words()
    print(checked[1])

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
