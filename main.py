import sys

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

from stats import word_count, get_char_counts, sorted_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)
    word_count_result = word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")
    char_counts = get_char_counts(book_text)
    sorted_counts = sorted_char_counts(char_counts)
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()