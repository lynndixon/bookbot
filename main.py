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

main_book_path = 'books/frankenstein.txt'

def main():
    book_text = get_book_test(main_book_path)
    print(f"{book_text}")
    return book_text

main()