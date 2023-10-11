#defined a function that reverses the user´s input
def is_palindrome(user):
    reversed_user = "" #created an empty variable
    for x in user: #using a for loop to reverse the input
        reversed_user = x + reversed_user #using contcatenation to establish reversing
    return user == reversed_user #checking if input and reversed input are equal, it will return true if it equal and print printstatement on ine 12 otherwise line 15

#getting users input
user = input("Please enter a word: ")

#outout
if is_palindrome(user):
    print(f"is a palindrome")
else:
    print(f"is not a palindrome")
