def get_num_words(text):
    wc = 0
    for word in text.split():
        wc += 1
    return wc

