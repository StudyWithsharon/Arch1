#get date from the user
date_input = input("Enter a date (YYYY-MM-DD): ")

def date_successor(year, month, day):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #create a list to determine how many days each month has, starting with index 0

    if day < days_in_month[month]:
        return year, month, day + 1 #returns day within the same month
    elif month < 12: #when it can´t return the next day within the same month it checks the month is not december
        return year, month + 1, 1 #returns year and next month and first day 
    else:
        return year + 1, 1, 1 #returns year +1 (increment) turning over to the next year and sets the month and day to 1(first)
        
#check if it is a valid input, first checking if the total input counts a total of 10 characters, then it checks if characters at position 4 and 7 are hyphens "-"
if len(date_input) == 10 and date_input[4] == date_input[7] == '-':
    try:
        year, month, day = map(int, date_input.split('-'))#here we assign a new variable to values from date_input we use split and determine to split everthing between hyphens en format the values into integers
        if 1 <= month <= 12 and 1 <= day <= 31: #checks if the month and day are within there proper range
            successor_year, successor_month, successor_day = date_successor(year, month, day)
            print(f"Next date: {successor_year:04d}-{successor_month:02d}-{successor_day:02d}")
        else:
            print("Invalid date values.")
    except ValueError: #error handling when user input is invalid
        print("Invalid input. Please use numbers for year, month, and day.")
else:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
