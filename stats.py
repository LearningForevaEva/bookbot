def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    result = {}
    lower_case = text.lower()
    for letter in lower_case:
        count = result.get(letter, 0)
        result[letter] = count +1
    return result

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list