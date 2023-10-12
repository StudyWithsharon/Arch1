def unique_chars_dict(s):
    char_dict = {}  #create empty dictioanry
    for char in s:
        if char.isalpha():  #check if there is alphabetical character
            char_dict[char] = char_dict.get(char, 0) + 1  #check if in dictionary if not add it and give it number 1

    return len(char_dict)  

def unique_chars_set(s):
    char_set = set()  #create empty set

    for char in s:
        if char.isalpha():  
            char_set.add(char)  

    return len(char_set)  

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    unique_chars_dict_count = unique_chars_dict(user_input)
    print(f"Using dictionaries, unique characters: {unique_chars_dict_count}")

    unique_chars_set_count = unique_chars_set(user_input)
    print(f"Using sets, unique characters: {unique_chars_set_count}")
