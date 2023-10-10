#asking user input with input function and since user input is a string by default we use "int" to convert it to an integer so we can make calculations with the users input
years = int(input("Enter the number of years: "))

#creating new variables to save results to 
months = years * 12
days = years * 365

#using an f-string to print result/output 
print(f"Months:{months}, days: {days}")
