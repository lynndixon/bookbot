from stats import get_num_words, get_chars_dict, sort_chars, format_chars
import sys


def main():
    try:
        book_path = get_book_path()
    except Exception as e:
        print(f"{e}")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars = sort_chars(chars_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")    
    print(f"--------- Character Count -------")
    print(format_chars(sorted_chars))
    print(f"============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_path():
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    return sys.argv[1]



main()
