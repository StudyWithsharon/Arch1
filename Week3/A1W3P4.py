#choosing to have 2 functions instead of 1 each taking one argument
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return int(round(fahrenheit, 0)) #using round so we don´t get a ridiculous long number

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return int(round(celsius, 0))

#examples
celsius_temperatures = [1, 10, 20, 30]
fahrenheit_temperatures = [celsius_to_fahrenheit(temp) for temp in celsius_temperatures]


print("°C °F")
for celsius, fahrenheit in zip(celsius_temperatures, fahrenheit_temperatures): #we use zip function to iterate over 2 lists
    print(f"{celsius} {fahrenheit}")
