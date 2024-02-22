def main():
    location = "books/frankenstein.txt"
    text = book_Text(location)
    num_words = word_Count(text)
    print(f"There are {num_words} words in the book!")
    num_letters = letter_Count(text)
    sorted_num_letters = sort_dictionary(num_letters)
    
    for item in sorted_num_letters:
        print(f"The {item['letter']} character was found {item['num']} times")

# function to take a books location and return the full text of the book
def book_Text(book_location):
    with open(book_location)as f:
        book_contents = f.read()
        return book_contents

# Count the number of words in a book
def word_Count(book):
    count = 0
    words = book.split()
    for word in words:
        count +=1
    return count

# Create a dictionary of the number of each letter in the book
def letter_Count(book):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z']
    count = 0
    letters = dict.fromkeys (alphabet, count)
    lowered_book = book.lower()

    for a in alphabet:
        for c in lowered_book:
            if c == a:
                letters[a] += 1
    return letters

# sorts a passed in dictionary on the num value
def sort_on(dictionary):
    return dictionary["num"]

# takes a dictionary and puts the entries into a list - the list is then sorted using sort_on
def sort_dictionary(dictionary):
    sorted_list = []
    for entry in dictionary:
        sorted_list.append({"letter": entry, "num": dictionary[entry]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()