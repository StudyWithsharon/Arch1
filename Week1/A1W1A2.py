#asking user input and converting it to a float(decimal number)
meal_costs = float(input("Cost of the meal: "))

#calculation: in this calculation we save the results into new variables and also round the result
tax = round(meal_costs * 0.21, 3) #", 3" we round the result to 3 decimal places
tip = round(meal_costs * 0.15, 3)
total = round(meal_costs + tax + tip, 3)

#and yet we use another f-string and yes also I rounded the results to 3 decimals, which was unnecessary
print(f"Tax: {tax:.3f}, Tip: {tip:.3f}, Total: {total:.3f}")
