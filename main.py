from collections import Counter


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    len_text = _get_number_of_words(text)
    count_characters = _get_char_count_in_the_string(text)
    # print(text)
    # print(len_text)
    # print(count_characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{len_text} words found in the document")
    for char, count in count_characters.items():
        print(f"The '{char}' character was found {count} times")
    print(f"--- End report of {book_path} ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def _get_number_of_words(text):
    return len(text.split())

def _get_char_count_in_the_string(text):
    # return Counter(text.lower())
    text_lowercase = text.lower()
    char_count = {}
    for char in text_lowercase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()
