def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    result = {}
    lower_case = text.lower()
    for letter in lower_case:
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result