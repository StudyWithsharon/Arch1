"""
Lists are mutable objects in Python. They are created by using with [ ]. Items are seperated by " , ". There are many ways to manipulate a list

1. .append()
2. .extend()
3. .insert()
4. .remove()
5. .reverse()

"""
#let´s add an item to the list
careers = ["painter", "fisherman", "policeman", "teacher"]
careers.append("singer")
#updated list--> ["painter", "fisherman", "policeman", "teacher", "singer"]

#let´s add a list into another list
toolbox = ["hammer", "saw", "screwdriver", "nails"]
careers.append(toolbox)
#updated list -->["painter", "fisherman", "policeman", "teacher", ["hammer", "saw", "screwdriver", "nails"]]


numbers1 = [1, 2, 3, 4, 5, 6, 7]
nubers2 = [8, 9, 10]



fruits = ["orange", "cherry", "apple", "pear", "melon"]
colors = ["red", "green", "blue", "brown", "yellow", "pink"]
