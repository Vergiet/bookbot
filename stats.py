def get_word_count(book_text):
    return len(book_text.split())

def get_character_count(book_text):

    char_list = list()
    count_dict = dict()

    for word in book_text.split():
        for char in word.lower():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1

    return count_dict

def sort_on(dict):
    return dict["num"]

def sort_character_count(count_dict):

    char_list = list()
    for char in count_dict:
        dict = {
            "char": char,
            "num": count_dict[char]
        }
        char_list.append(dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list