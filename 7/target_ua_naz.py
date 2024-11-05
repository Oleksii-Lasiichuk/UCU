"""
Ukrainian target game
"""
from random import choice
def generate_grid() -> list[str]:
    """
    Generates grid for round
    Returns:
        list[str]: list of letters for the play
    """
    alpha_lst = ["а", "б", "в", "г", "ґ", "д", "е", "є", "ж",\
"з", "и", "і", "ї", "й", "к", "л", "м", "н", "о", "п", "р", "с",\
"т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ю", "я"]
    game_lst = []
    while len(game_lst) < 5:
        letter = choice(alpha_lst)
        if letter not in game_lst:
            game_lst.append(letter)
    return game_lst

def get_words(file_name: str, letters: list[str]) -> list[tuple]:
    """
    Opens file and checks for needed words
    Args:
        file_name (str): name of file to open
        letters (list[str]): letters to check
    Returns:
        list[tuple]: list of tuple - wprd + part of language
    >>> get_words("base.lst", ['щ'])
    [('щасні', 'noun'), ('щасно', 'adverb'), ('щастя', 'noun'), ('ще', 'adverb'), \
('щебет', 'noun'), ('щем', 'noun'), ('щемно', 'adverb'), ('щеня', 'noun'), \
('щепа', 'noun'), ('щерба', 'noun'), ('щигля', 'noun'), ('щипак', 'noun'), \
('щипок', 'noun'), ('щипці', 'noun'), ('щир', 'noun'), ('щирий', 'adjective'), \
('щит', 'noun'), ('щиток', 'noun'), ('щі', 'noun'), ('щіпка', 'noun'), ('щітка', 'noun'), \
('щіть', 'noun'), ('щічка', 'noun'), ('щогла', 'noun'), ('щодва', 'adverb'), \
('щодві', 'adverb'), ('щодня', 'adverb'), ('щока', 'noun'), ('щоніч', 'adverb'), \
('щораз', 'adverb'), ('щорік', 'adverb'), ('щотри', 'adverb'), ('щука', 'noun'), \
('щуп', 'noun'), ('щупак', 'noun'), ('щупик', 'noun'), ('щупля', 'noun'), \
('щур', 'noun'), ('щурик', 'noun'), ('щурка', 'noun'), ('щуря', 'noun'), \
('щучий', 'adjective'), ('щучин', 'adjective'), ('щучка', 'noun')]
    """
    with open(file_name, "r", encoding="utf-8") as file:
        file_lst = []
        check_lst = ["adv", "/adj", "noun", "verb", "/v", "/n"]
        for line in file:
            word = ''
            part_of_speech = ''
            line = line.replace("\n", "")
            for k in check_lst:
                if k in line:
                    if k == 'adv':
                        part_of_speech = 'adverb'
                    if k == '/adj':
                        part_of_speech = 'adjective'
                    if k in ("noun", '/n'):
                        part_of_speech = 'noun'
                    if k in ('/v', "verb"):
                        part_of_speech = 'verb'
            if part_of_speech != "":
                for i in line:
                    if i == " ":
                        break
                    word += i
            if len(word) != 0:
                if len(word) <= 5 and word[0] in letters and (word, part_of_speech) not in file_lst:
                    file_lst.append((word, part_of_speech))
    return file_lst

def check_user_words(user_words: list[str], language_part: str,\
letters: list[str], dict_of_words: list[tuple]) -> tuple[list]:
    """
    Checks for right and missed words
    Args:
        user_words (list[str]): words of user
        language_part (str): part of language
        letters (list[str]): letters
        dict_of_words (list[tuple]): words which match
    Returns:
        tuple[list]: list of player right words and list of words he missed
    """
    player_win_lst = []
    for i in user_words:
        if i[0] in letters:
            for k in dict_of_words:
                if i in k[0] and i not in player_win_lst:
                    player_win_lst.append(i)
    skip_lst = []
    for i in dict_of_words:
        if i[0] not in player_win_lst and i[1] == language_part:
            skip_lst.append(i[0])
    return player_win_lst, skip_lst
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
