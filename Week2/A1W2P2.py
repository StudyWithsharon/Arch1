def main():
    year = int(input("Enter a year: ")) #asking user input and converting into an int

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

def is_leap_year(year):
    if year % 400 == 0: #"%" gives the remainder of a devision and checks if it is equel to 0 and returns a true or false
        return True
    elif year % 100 == 0: 
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == "__main__": #starting point of execution, does not take arguments, checks if script is being imported or can run directly
    main()
    
