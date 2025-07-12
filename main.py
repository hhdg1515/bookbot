import sys
from stats import get_num_words, get_char_counts, get_sorted_char_list

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = get_char_counts(text)
    sorted_chars = get_sorted_char_list(char_counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()


