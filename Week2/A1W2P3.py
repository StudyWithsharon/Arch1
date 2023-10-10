# now we need to process this input, I don't know that much yet, so I guessed to use def, else, elif, etc. also for this problem
def identify_shape(user_input): #did some more research on functions they are the main building blocks and you can pretty much create almost any functins you can imagine
    if user_input == 4:
        return "square"
    elif user_input == 5:
        return "pentagon"
    elif user_input == 3:
        return "triangle"
    elif user_input == 6:
        return "hexagon"
    elif user_input == 8:
        return "octagon"
    elif user_input == 10:
        return "decagon"
    else:
        return "unknown shape"

# so now we defined the shapes, but the user will not see anything so here is the output
def main():
    try:
        user_input = int(input("Enter the number of sides(as an integer): "))
        if 3 <= user_input <= 11:
            shape_ID = identify_shape(user_input)
            print(f"The number {user_input} represents the shape {shape_ID}")
        else:
            print(f"Amount of sides is out of range")
    except ValueError: #error handling
        print("Amount of sides is out of range")

# Calling the main function
if __name__ == "__main__": #this line is a special construct in Python, so we can change  def "main" to whatever but this line makes sure it runs directly but for convinient purposes I call the function main
    main()#changeable
