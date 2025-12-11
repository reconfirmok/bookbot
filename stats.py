def get_book_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lower_text = text.lower()
    char_dict = {}

    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict


def sort_on(chars):
    return chars["num"]


def sorted_dict(chars_dict):
    key_value_list = []

    for key in chars_dict:
        new_dict = {"char": key, "num": chars_dict[key]}
        key_value_list.append(new_dict)

    key_value_list.sort(reverse=True, key=sort_on)
    return key_value_list