def get_book_test(path):
    text = ""
    with open(path) as f:
        text = f.read()
    return text

def get_word_count(text):
    wc = 0
    for word in text.split():
        wc += 1
    return wc;

def main():
    path = "books/frankenstein.txt" 
    print(f"{get_word_count(get_book_test(path))} words found in the document")

main()
