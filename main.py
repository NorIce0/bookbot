from stats import get_num_words, get_char_count, clean_data

def get_book_test(path):
    text = ""
    with open(path) as f:
        text = f.read()
    return text

def main():
    path = "books/frankenstein.txt" 
    char_data = clean_data(get_char_count(get_book_test(path)))

    print("============ BOOKBOOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count -----------")
    
    print(f"Found { get_num_words(get_book_test(path)) } total words")
    
    print("--------- Character Count ---------")

    for data_point in char_data:
        if data_point["char"].isalpha():
            print(f"{data_point['char']}: {data_point['num']}")
    
    print("============= END =============")


main()
