def is_integer(unchecked: str):
    unchecked = unchecked.strip()  #removing whitespaces

    if len(unchecked) >= 1:  #checking if length is at least 1
        if unchecked[0] in ("+", "-") and len(unchecked) > 1:
            return unchecked[1:].isdigit()  #checks if characters are digits
        return unchecked.isdigit()
    return False


def remove_non_integer(unchecked: str) -> int:  #converts to integer
    cleaned = ''.join(char for char in unchecked if char.isdigit() or char in ('+', '-'))
    return int(cleaned)


if __name__ == "__main__":
    user_input = input("Enter something: ") #this is the main part were user is asked to input something

    if is_integer(user_input):  #it calls function: is_integer for user input to check it
        print("Valid integer")
        print(f"Cleaned integer: {remove_non_integer(user_input)} ")
    else:
        print("Invalid integer")
