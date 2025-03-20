from stats import count_words
from stats import get_book_text

def main(): 
    filepath = "/home/andrue/workspace/github.com/Yuri-Undertones/bookbot/books/frankenstein.txt"
    text = get_book_text(filepath)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

main()