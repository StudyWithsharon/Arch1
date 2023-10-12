"""
Lists are mutable objects in Python. They are created by using with [ ]. Items are seperated by " , ". There are many ways to manipulate a list
Keep in mind: sequence [start:stop:step]

1. .append()
2. .extend()
3. .insert()
4. .remove()
5. .reverse()

"""
#ADDING ITEMS
careers = ["painter", "fisherman", "policeman", "teacher"]
careers.append("singer")
#updated list--> ["painter", "fisherman", "policeman", "teacher", "singer"]

#ADD LIST WHITHIN A LIST
toolbox = ["hammer", "saw", "screwdriver", "nails"]
careers.append(toolbox)
#updated list -->["painter", "fisherman", "policeman", "teacher", ["hammer", "saw", "screwdriver", "nails"]]

#COMBINE TWO LISTS TOGETHER
numbers1 = [1, 2, 3, 4, 5, 6, 7]
numbers2 = [8, 9, 10]
numbers1.extend(numbers2)
#updated list --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#INSERTING ITEMS
fruits = ["orange", "cherry", "apple", "pear", "melon"]
fruits.insert(0, "coconut")
#updated list --> ["coconut", "orange", "cherry", "apple", "pear", "melon"]

#REMOVE ITEMS
fruits = ["orange", "cherry", "apple", "pear", "melon"]



fruits = ["orange", "cherry", "apple", "pear", "melon"]
colors = ["red", "green", "blue", "brown", "yellow", "pink"]
