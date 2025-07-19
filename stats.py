def word_count(text):
    words = text.split()
    return len(words)

def no_each_character(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts