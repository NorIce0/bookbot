def get_book_test(path):
    with open(path) as f:
        print(f.read())

def main():
    get_book_test("books/frankenstein.txt")

main()
