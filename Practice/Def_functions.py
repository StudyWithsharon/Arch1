#DEF BASISCS

def sum(a, b):
    return a + b 
print(sum(20, 2))


def say_my_name():
    print("Hello Sharon")
    
#you have to call a function in order for it to run
say_my_name()

def say_my_name2(name):
    print(name)
    
say_my_name2()
#multiple arguments and default arguments. There are positional arguments and named arguments
def greeting(greet, name "Hola"):
    print(f"{name} {name}")


def empty_function():
    Pass #you can create an empty function using Pass




#AGE CHECKER

#practice to define functions with def

def greeting():
    name = input("Enter  your name: ")
    age = int(input("Enter your age: "))
    if age >= 18:
        print("Welcome")
        
    else:
        print("Sorry you are not old enough")
        
greeting()

#you can make a default argument




#TIP CALCULATOR

def calculate_food_total(food_amount, tip_percentage):
    tip_amount = food_amount * (tip_percentage / 100)
    total_amount = tip_amount + food_amount
    print(tip_amount)
    print(total_amount)
calculate_food_total(10, 10) #calling the function with arguments, the argument




#WORD FREQUENCY
# creating a function that keeps track of word frequency and puts them into a dictionary

def word_frequency(phrase):
    result = {}
    words = phrase.split()
    for word in words:
        if word not in result:
            result[word] = 1 
        else:
            result[word] += 1
    return result

print(word_frequency("What a beautiful day, just like yesterday when it was also beautiful"))
