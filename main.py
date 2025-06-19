def get_book_test(filepath):
    """
    Reads a book from a given file path and returns its content.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        book_content = file.read()
    return book_content

def count_num_words(book_text):
    """
    Counts the number of words in the given book text.
    
    Args:
        book_text (str): The content of the book.
        
    Returns:
        int: The number of words in the book.
    """
    words = book_text.split()
    print(f"{len(words)} words found in the document")
    return len(words)


main_book_path = "books/frankenstein.txt"

def main():
    book_text = get_book_test(main_book_path)
    num_words = count_num_words(book_text)
    return

main()