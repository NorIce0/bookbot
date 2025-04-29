from stats import get_num_words, get_char_count

def get_book_test(path):
    text = ""
    with open(path) as f:
        text = f.read()
    return text

def main():
    path = "books/frankenstein.txt" 
    char_count = get_char_count(get_book_test(path))

    print(f"{get_num_words(get_book_test(path))} words found in the document")
    print(f"{char_count}")


main()
