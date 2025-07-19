def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def word_count(text):
    words = text.split()
    return len(words)

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    word_count_result = word_count(book_text)
    print(f'{word_count_result} words found in the document.')
    # Further processing of book_text can be done here



main()