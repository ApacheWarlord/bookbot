def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    print(book_text)
    # Further processing of book_text can be done here



main()