def get_num_words(text):
    wc = 0
    for word in text.split():
        wc += 1
    return wc

def get_char_count(text):
    char_count = {}
    for c in text.lower():
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def clean_data(data):
    keys = []
    for key in data.keys():
        keys.append({"char": key, "num": data[key]})
    keys.sort(key = get_count, reverse = True)
    return keys

def get_count(data_point):
    return data_point["num"]
