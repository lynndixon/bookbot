from stats import get_num_words, get_chars_dict, sort_chars, format_chars


def main():
    book_path = "books/frankenstein.txt"
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

main()
