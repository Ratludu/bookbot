from stats import num_words, character_count, sorted_list
import sys

def get_book_text(file_path: str) -> str:
    
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book = sys.argv[1]
    _text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words(_text)} total words")
    print("--------- Character Count -------")
    
    for key, value in sorted_list(character_count(_text)).items():

        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
