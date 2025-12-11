from stats import get_book_words


def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = get_book_words(book_content)
    print(f"Found {num_words} total words")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()