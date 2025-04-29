from stats import get_num_words

def get_book_test(path):
    text = ""
    with open(path) as f:
        text = f.read()
    return text

def main():
    path = "books/frankenstein.txt" 
    print(f"{get_num_words(get_book_test(path))} words found in the document")

main()
