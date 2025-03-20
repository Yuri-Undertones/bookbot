def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    character_counts = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def sort_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_data = {"char": char, "count": count}
        char_list.append(char_data)
    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list 

    


