def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text):
    chars = {}
    for char in text:
        lowered_case = char.lower()
        if lowered_case in chars:
            chars[lowered_case] += 1
        else:
            chars[lowered_case] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list