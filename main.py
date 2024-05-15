def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = get_letter_counts(text)
    print_report(book_path, num_words, letter_counts)


def print_report(book_path, num_words, letter_counts):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} found in the document")
    print()
    for l in letter_counts:
        print(f"The '{l['letter']}' character was found {l['count']} times")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_letter_counts(text):
    letter_counts = []
    character_counts = get_character_counts(text)
    for c in character_counts:
        if c.isalpha():
            letter_counts.append({
                "letter": c,
                "count": character_counts[c]
            })
    letter_counts.sort(reverse=True, key=lambda x: x['count'])
    return letter_counts


def get_character_counts(text):
    character_counts = {}
    for c in text.lower():
        if c not in character_counts:
            character_counts[c] = 0
        character_counts[c] += 1
    return character_counts


main()
