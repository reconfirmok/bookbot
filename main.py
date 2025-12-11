from stats import (
    get_book_words,
    get_num_characters,
    sorted_dict
    )


def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = get_book_words(book_content)
    num_chars = get_num_characters(book_content)
    dict_sorted = sorted_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in dict_sorted:
        if dict["char"].isalpha() == False:
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()