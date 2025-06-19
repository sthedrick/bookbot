from stats import *
import sys

def analyze_book(bookFilePath):
    booktext = ""

    print(f"Analyzing book found at {bookFilePath}...")
    booktext = get_book_text(bookFilePath)
    
    print("----------- Word Count ----------")
    words = get_num_words(booktext)
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    print_char_count(booktext)

    print("============= END ===============")



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    analyze_book(book_path)

    

main()
    


