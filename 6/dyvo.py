"""puts word диво in front of every word that starts with flag"""
def insert_dyvo(sentence, flag):
    """
    Вставляє 'диво' перед кожним словом, яке починається з певного прапора

        1 4 6
    #     Testing dyvo
    # Test1: Failed
    # кит
    # Test2: Failed
    # Кит кота по хвилях катав - кит у воді, кіт на киті.
    # Test3: Failed
    # Босий хлопець сіно косить, роса росить ноги босі.
    # Test4: Failed
    # 1234
    # Test5: Failed
    # Був собі цебер, та переполуцебрився на полуцебренята.
    # Test6: Failed
    # Пилип прилип, прилип Пилип. Пилип плаче. 
    # Пилип посіяв просо, просо поспіло, пташки прилетіли, просо поїли.


    >>> insert_dyvo('Кит кота по хвилях катав - кит у воді, кіт на киті', 'ки')
    'Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті'

    >>> insert_dyvo('Олексій був чоботарем, ходив у гарних чоботях, плив на прекрасному човні', "чо")
    'Олексій був дивочоботарем, ходив у гарних дивочоботях, плив на прекрасному дивочовні'

    >>> insert_dyvo('67', "чо")
    '67'
    """
    if not isinstance(sentence, str):
        return None
    words = sentence.split(" ")
    lenght_flag = len(flag)
    for i, word in enumerate(words):
        if word[0].isupper():
            if word[:lenght_flag] == flag.capitalize():
                words[i] = "Диво" + word.lower()
        else:
            if word[:lenght_flag] == flag:
                words[i] = "диво" + word
    return " ".join(words)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())