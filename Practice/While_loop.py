#BASIC WHILE LOOPS

x = 0 
while x < 10:
    print(x)
    x += 1

x = 0 
while x < 10:
    if x == 5:
        break #you can use a break statement to jump out of the loop
    print(x)
    x += 1




#INFINITE WHILE LOOP

#be careful with while loops because you can easily create an infinite loop
sharon = "sleeping"
while sharon != "sitting":
    print("keep on looping")




#SETTING A CONDITIONAL WHILE LOOP

#be careful with while loops because you can easily create an infinite loop. Make sure you have a statement to allow them to break/stop
counter = 0
while counter < 11: #setting a condition for the loop so once the condition is met the loop stops
    print(counter)
    counter = counter + 1 #incrementing counter by 1


 
#it can also be written like this

counter = 0
while counter < 11: 
    print(counter)
    counter += 1 #incrementing counter by 1




