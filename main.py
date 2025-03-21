import sys

from stats import count_words, count_characters, character_stats


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        text = f.read()
        return text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    word_count = count_words(text)
    character_counts = count_characters(text)
    stats = character_stats(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for stat in stats:
        if stat["character"].isalpha():
            print(f"{stat["character"]}: {stat["count"]}")
    print("============= END ===============")
    sys.exit(0)


if __name__ == "__main__":
    main()
