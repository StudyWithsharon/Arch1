import random  #importing library that genereates random numbers

def arithmetic_operation(arithmetic_type):
    mistakes = []  #creating an empty list to store the mistakes

    for _ in range(10):  #create a a loop that will run 10 times to generate 10 execercises
        num1 = random.randint(1, 100)  #create a random number 1
        num2 = random.randint(1, 100)  #create a random number 2

        #this is the main operation that will determine the outcome of the math problem there are 3 different math types described
        if arithmetic_type == "summation":
            operation = f"{num1} + {num2} = "
            result = num1 + num2
        elif arithmetic_type == "multiplication":
            operation = f"{num1} * {num2} = "
            result = num1 * num2
        elif arithmetic_type == "subtraction":
            operation = f"{max(num1, num2)} - {min(num1, num2)} = "
            result = max(num1, num2) - min(num1, num2)
        else:
            print("Invalid arithmetic type.")
            return

        user_answer = input(operation)

        if not user_answer.isdigit() or int(user_answer) != result:  #checks if user gives valid input
            mistakes.append(operation + str(result))  #this line is responsible for saving mistakes to the mistake list

    return mistakes

#ask user what math operation user wants to practise
if __name__ == "__main__":  #using if __name__ block to ensure the within it only runs
    arithmetic_type = input("Which math operation would you like to practice? (summation, multiplication, subtraction): ")
    mistakes = arithmetic_operation(arithmetic_type)

# Print the mistakes
if mistakes:
    print("\nMistakes:")
    for mistake in mistakes:  #mistakes will be printed one by one
        print(mistake)
else:
    print("You've completed all exercises correctly!")  #if no mistakes this line will be printed
