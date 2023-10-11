def is_palindrome(input_str):
    input_str = input_str.replace(" ", "")  #this time we have to remove spaces
    return input_str == input_str[::-1]  #this time not using a look to reverse


user_input = input("Please enter a word: ")
result = is_palindrome(user_input)


if result:
    print(f"'{user_input}' is a palindrome")
else:
    print(f"'{user_input}' is not a palindrome")
 Missing newline at the end of file.
