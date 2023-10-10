#we ask the user to enter a whole number aka integer
try:
    user_input = int(input("Please enter a whole number "))

#We need to check if the input is even or odd. We can do so by deviding the input by 2 and calculating the remainder with ==, when rmainder is 0 it results in a true meaningan even number
    if user_input % 2 == 0:
        print(f"{user_input} is an even number")
    #in this line we show false or in other words the odd number
    else:
        print(f"{user_input} is an odd number")
#in line 3 we asked user for an integer the int funciton in front of the input string converts input to int so when user enters a float it will result in an error
except ValueError:
    print("Your input was incorrect please enter a whole number")
    
