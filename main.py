def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(book_content)

main()