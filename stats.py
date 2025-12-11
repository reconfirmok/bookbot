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
