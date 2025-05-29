from stats import get_word_count, get_character_count, sort_character_count
import sys





def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
    return file_contents



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    real_bookspath = sys.argv[1]

    book_text = get_book_text(real_bookspath)
    word_count = get_word_count(book_text)
    char_count = get_character_count(book_text)
    sorted_char_count = sort_character_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {real_bookspath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for each in sorted_char_count:
        if each["char"].isalpha():
            print(f"{each["char"]}: {each["num"]}")
    print("============= END ===============")
    

main()