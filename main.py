from stats import count_words, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    characters = character_count(text)
    print(f"Found {word_count} total words")
    print(characters)

if __name__ == "__main__":
    main()