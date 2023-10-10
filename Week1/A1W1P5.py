#Input user
number_input = int(input("Please enter a 4-digit number here ")) 

#Process step 1 in order to add each digit to the other we first need to extract the digits got instructions from google
#Formula for extrating is to divide by 10 and for digit in the hunderds and tens we need to ad a %modulus in order to get the digit
digit1 = number_input // 1000
digit2 = (number_input // 100) % 10
digit3 = (number_input // 10) % 10
digit4 = number_input % 10

#Process step 2 adding all the digits
sum_digits = digit1 + digit2 + digit3 + digit4

#Output result usinf a f string
print(f"{digit1}+{digit2}+{digit3}+{digit4}={sum_digits}.")
