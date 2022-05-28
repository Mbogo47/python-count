import re

def read_file_content(filename):
    file = open(filename)
    data = file.read()
    return data


def count_text(word, list):
    result = 0
    for element in list:
        if element == word:
            result += 1
    return result

def count_words():
    text = read_file_content("story.txt").lower()
    dict = {}
    pattern = r'[^A-Za-z0-9]+'
    text_list = re.sub(pattern, ' ', text).split(' ')
    unique_words = sorted(list(set(text_list)))
    all_counted_words = []

    for word in unique_words:
        count = count_text(word, text_list)
        dict = {word: count}
        all_counted_words.append(dict)

    print(all_counted_words)

count_words()