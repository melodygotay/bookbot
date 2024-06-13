from collections import Counter
from collections import OrderedDict
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def word_counter():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        words = book.split()
        return (len(words))

def character_counter():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        lowercase = book.lower()
        string = lowercase.split()
        #splits the text into words

        counter_dict = {}
        for words in string: #iterates over words in string
            for letter in words: #iterates over letters in words
                if letter.isalpha() == True: #filters non alphabet characters
                    counter_dict.setdefault(letter, 0) #setdefault initializes your dict
                    counter_dict[letter] += 1

        ordered = OrderedDict(sorted(counter_dict.items(), key=lambda x: x[1], reverse=True))
        #orders counter_dict by key 1. Sorted does not allow arguments, so we use "lambda" to be able to do so.
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_counter()} words found in the document")
        print()
        for letters in ordered:
            num = ordered[letters]
            counter_dict[letters] = num
            print(f"The '{letters}' character was found {num} times")
        print("--- End report ---")
    
if __name__ == "__main__":
    main()
    word_counter()
    character_counter()