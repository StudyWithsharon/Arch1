my_tuple = 1, 2, 3, 4, 5  # immutable

my_list = ["apple", "pear", "coconut", "peach"]  # mutable

my_dictionary = {
    "The Old Man and The Sea": "Ernest Hemingway",  # mutable
    "Lord of The Flies": "William Golding",
    "The Trial": "Franz Kafka",
}

my_variable = "This is a string"  # immutable

A = 7

#using methods
print(int(sum(my_tuple)))  # calculates the sum of the numbers in the tuple like: 1+2+3+4+5 Returns 15

print(my_dictionary.items())

print(type(my_variable))

print(my_list.count("apple"))

print(A)
print(type(A))

my_list.append("melon") # add a item to a list
print(my_list)

my_list.insert(2, "cherry") # inserting a new item to the list at a specific location
print(my_list)

print(my_list.index("cherry")) # getting the position/index the list

new_variable = my_variable[1:4] # slicing
print(new_variable)

new_element = my_tuple[2] # selecting a element with offset method
print(new_element)

# reversing items  can be done by using  reverse or slicing

# reversing using reverse
veggies = ["eggplant", "pumpkin", "tomato", "lettuce"]
veggies.reverse()
print(veggies)
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.reverse()
print(numbers)

# reversing using slicing

al = ["a", "b", "c", "d", "e"]
la = al[::-1]
print(la)

b = [10, 11, 12, 13, 14, 15, 16, 17]
c = b[1:5:2]
print(c)
