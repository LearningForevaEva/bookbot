from stats import (
    count_words,
    character_count,
    chars_dict_to_sorted_list,
)
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    characters = character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(characters)
    print_report(book_path, word_count, chars_sorted_list)

def print_report(book_path, word_count, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
if __name__ == "__main__":
    main()