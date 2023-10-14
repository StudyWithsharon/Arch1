#changing a value in a dictionary

def library():
    book = {
        "Brave New World": "Aldous Huxley",
        "1984": "George Orwell",
        "The Red Pony": "John Steinbeck",
        "A list within a dictionary": ["orange", "apple", "strawberry"]
    }
    return book  #return the book dictionary

library_data = library()  #call the library function and store the result in library_data

#modify the value associated with the key "1984"
library_data["1984"] = "funny"

print(library_data)  #print the updated book dictionary

#you can´t change a key from a dictionary directly

def rename_key(dictionary, old_key, new_key):
    if old_key in dictionary:
        dictionary[new_key] = dictionary.pop(old_key)

#example usage:
book = {
    "Brave New World": "Aldous Huxley",
    "1984": "George Orwell",
    "The Red Pony": "John Steinbeck"
}

#rename the key "1984" to "Nineteen Eighty-Four"
rename_key(book, "1984", "Nineteen Eighty-Four")

print(book)
