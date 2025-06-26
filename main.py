import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")

def main(filepath):
    book_text = get_book_text(filepath)
    word_count = num_words(book_text)
    character_counts = character_count(book_text)
    report_dict = report_gen(character_counts)
    print("============ BOOKBOT ============")
    print(f"Analayzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in report_dict:
        print(f"{item["char"]}: {item["num"]}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

from stats import character_count

from stats import report_gen

#try:
main(sys.argv[1])
#except exception as e:
#    print(Usage: python3 main.py <path_to_book>)
