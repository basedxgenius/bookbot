def get_num_words(text):
    words = text.split()
    return len(words)
def character_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in [' ', '\n']:
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
def sort_on(char_dict):
    return char_dict["num"]

def sort_characters(char_count_dic):
    sorted_chars = []
    for char, count in char_count_dic.items():
        sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(key=sort_on, reverse=True)
    return sorted_chars
