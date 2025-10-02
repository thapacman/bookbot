import sys
from stats import word_count
from stats import char_count
from stats import sort_dict

def get_book_text(path):
    file_contents = path.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    entered_path = sys.argv[1]
    print(entered_path)
    with open(entered_path) as f:
        print("============ BOOKBOT ============")
        book_text = get_book_text(f)
        print(f"Analyzing book found at {entered_path}...")
        print("----------- Word Count ----------")
        character_dictionary = char_count(book_text)
        print(f"Found {word_count(book_text)} total words")
        print("--------- Character Count -------")
        sorted_character_dictionary = sort_dict(character_dictionary)
        for i in range(0, len(sorted_character_dictionary)):
            letter = sorted_character_dictionary[i]["character"]
            number = sorted_character_dictionary[i]["count"]
            print(f"{letter}: {number}")
        print("============= END ===============")
main()