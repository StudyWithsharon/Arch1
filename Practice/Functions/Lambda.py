"""Lambda allows you to vreate an anonymous function. Lambda is a quick way to create a single line function. Bur for more complex functions we need to use def
   Also in Lambda you don´t need a return statement. 
"""

#ADDING 2 NUMBERS
sum1 = lambda a, b: a + b
print(sum1(2, 10))

#ADDING 3 NUMBERS
sum2 = lambda c, d, f: c + d + f
print(sum2(2, 8, 5))

#REVERSING A STRING
reversing = lambda x: x[::-1]
print(reversing("Hello how are you?"))

#COMBINE MULTIPLE LAMBDA FUNCTIONS
add = lambda y, z: y + z
multiply = lambda w: w * 2

result = multiply(add(2, 8))
print(result)

#SORTING
students = [
    {'name': 'Alice', 'age': 22},
    {'name': 'John', 'age': 32},
    {'name': 'Frank', 'age': 42}
]

sorted_students = sorted(students, key=lambda x: x["age"])
print(sorted_students)
