#defining a function
def multiplication_table():
    print("\t", end="")  #creating whitespaces
    for a in range(1, 11): #using a for loop and setting a range of 10
        print(f"{a}\t", end="")  #"end="" " will make it continue on the same line
    print()  #creating whitespace

    
    for a in range(1, 11):
        print(f"{a}\t", end="")
        for b in range(1, 11):
            print(f"{a * b}\t", end="") 
        print()

#calling the function
multiplication_table()
