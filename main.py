import sys
from stats import get_num_words, character_count, sort_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # Check if a file path was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    # Load the book text from a file
    text = get_book_text(filepath)

    # Word count
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    # Character count
    print("--------- Character Count -------")
    char_counts = character_count(text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        print(f"{(item['char'])}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
