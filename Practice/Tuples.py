#BASICS
""" You create a tuple using only " " or using ( ). The items in a tuple are separated by commas just as in a list. 
    The main difference between e list and a tuple is that a tuple is NOT mutable.
"""
#assiging items from a tuple into variables
my_tuple = 1, 2, 3
a, b, c = my_tuple #assigned each item of the tuple to a variable

print(my_tuple)
print(a) #<-will print 1
print(b) #<-will print 2
print(c) #<-will print 3

#concatenate 2 tuples
just_a_tuple = 1, 2, 3 
another_tuple = 4, 5, 6, 7
new_tuple = just_a_tuple + another_tuple
print(new_tuple)





#TUPLES AND FOR LOOPS

def my_tuple(text1, text2, text3):
    return text1, text2, text3

result = my_tuple("hello", "hola", "hoi")
print(result)

a, b, c = my_tuple("hello", "hola", "hoi")
print(a, b, c)

for item in result:
    print(item)
