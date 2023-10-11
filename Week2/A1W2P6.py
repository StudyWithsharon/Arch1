#asking user input
human_age = int(input("Please enter a number: "))

#first we need to check if the user entered a positive number
if human_age < 0:
    print("The number you  entered is negative, please enter a positive number")
    
#second we need to count the first 2 human years as 10,5 dog years
elif human_age <= 2: #usig a comparison operator
    dog_age = human_age * 10.5
#third we need to count every other year after the first 2 years as 4 years
else:
    dog_age = 21 + (human_age - 2) * 4 

#telling the user how old they are in dog years using 2 options for output so to keep in mind that there are more ways to get the job done 
print(dog_age)
