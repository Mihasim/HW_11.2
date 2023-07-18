def get_title(new_string):
    return new_string.upper()


def get_title_letter(new_string):
    """:return word with tittle letter"""
    list_word = []
    for word in new_string.split():
        list_word.append(word.title())
    return ' '.join(list_word)