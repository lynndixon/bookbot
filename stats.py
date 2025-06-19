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

def count_num_characters(book_text):
    book_lower = book_text.lower()
    char_counts = {}
    for char in book_lower:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        print(f"'{char}': {count}")
    return char_counts