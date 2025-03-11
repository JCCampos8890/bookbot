def get_num_words(text):
    return len(text.split())

def counting_chars(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sorted_list(char_count):
    return sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    