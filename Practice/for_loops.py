#CREATING A NUMBERED LIST 1

#iterating over a sequence is called traversal

fruits = ["apple", "cherry", "orange", "clementine", "grape"]

for fruit in enumerate(fruits): #<-using the enumerate function to show the index/postion of our items
    print("Fruit:", fruit) #the word fruit has to match with the word fruit in above line, they can be other words or letters like x as long as they match

#the code above will print the following:
#Fruit: (0, "aple")
#Fruit: (1, "cherry")
#Fruit: (2, "orange")
#Fruit: (3, "clementine")
#Fruit: (4, "grape")




#COMBINING LISTS WITH FOR LOOP 2

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
#type your answer here.
for item in lst1:
    lst2.append("Dr." +item)

print(lst2)

fruits = ["cherry", "blueberry", "banana"]
colors = ["red", "blue", "yellow"]

fruit_color_pairs = []

for i in range(len(fruits)):
    fruit = fruits[i]
    color = colors[i]
    fruit_color_pairs.append((fruit, color))

print(fruit_color_pairs)

animals = ["Polar Bear", "elephant", "monkey"]
place = ["North Pole", "Africa", "Jungle"]

animal_place_pair = []

for x in range(len(animals)):
    animal = animals[x]
    places = place[x]
    animal_place_pair.append((animal, places)) #<-- make sure you have 2 parantheses if you use 2 arguments
print(animal_place_pair)



#DOUBLE THE NUMBER WITH A FOR LOOP

#assignment it to double the numbers from the list above. Output should be: [2, 4, 6, 8, 10]

def double(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return(result)
        
print(double([1, 2, 3, 4, 5,]))











