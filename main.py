from stats import *

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
    print("============ BOOKBOT ============")
    analyze_book("books/frankenstein.txt")

    

main()
    


