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