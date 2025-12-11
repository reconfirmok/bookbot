from stats import get_book_words, get_num_characters


def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = get_book_words(book_content)
    num_chars = get_num_characters(book_content)
    print(f"Found {num_words} total words")
    print(num_chars)


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()