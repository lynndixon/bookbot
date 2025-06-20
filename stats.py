def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_chars(chars_dict):
    # Create a list of dicts for each character (only alphabetic)
    chars_list = []
    for char, num in chars_dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": num})
    # Sort the list by 'num' in descending order
    return sorted(chars_list, key=sort_on, reverse=True)

def format_chars(chars_list):
    # Format the characters for display
    return "\n".join([f"{item['char']}: {item['num']}" for item in chars_list])