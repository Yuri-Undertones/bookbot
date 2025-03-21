import sys
from stats import count_words
from stats import get_book_text
from stats import count_letters
from stats import sort_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_counts = count_letters(text)
    sorted_chars = sort_list(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


main()