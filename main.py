def get_book_text(filepath):
    with open(filepath) as f:
    
        file_contents = f.read()

        #print (file_contents)

    wordcount = 0
    for w in file_contents.split():
        wordcount += 1

    print (f"{wordcount} words found in the document")
    return



def main():
    get_book_text("books/frankenstein.txt")


main()
    


