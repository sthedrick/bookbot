def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
    
        file_contents = f.read()
        return file_contents
    
def get_num_words(booktext):
    wordcount = 0
    for w in booktext.split():
        wordcount += 1

    print (f"Found {wordcount} total words")
    return

def print_char_count(booktext):
    #returns dictonary of {letter : count}
    char_dict = {}

    for char in booktext:
        char = char.lower()
        if char in char_dict:
            char_count = char_dict[char] + 1
        else:
            char_count = 1
        char_dict[char] = char_count

    #sort the dictionary
    sorted_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    
    for item in sorted_dict:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")

    return





    

