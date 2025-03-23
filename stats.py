
def num_words(_text: str) -> int:
    return len(_text.split())

def character_count(_text: str) -> dict:

    text_dict: dict = {}

    for letter in list(set(_text.lower())):

        text_dict[letter] = _text.lower().count(letter)

    return text_dict


def sorted_list(_text_dict: dict) -> list:

    sorted_dict = {key:val for key, val in sorted(_text_dict.items(), key = lambda item:item[1], reverse = True)}
    return sorted_dict
