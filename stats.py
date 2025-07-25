def word_count(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def sorted_char_counts(char_counts):
    # Create a list of dicts for alphabetic characters only
    char_list = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    # Sort by count descending
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
