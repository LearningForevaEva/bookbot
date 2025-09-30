from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = count_words(text)
    print(f"Found {word_count} total words")

if __name__ == "__main__":
    main()