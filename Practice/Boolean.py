#PASSING GRADE

score = int(input("Please enter a score to see if you have passed: "))

if score > 60 < 100:
    print("You passed the test")
else:
    print("you have failed the test")




#GRADE CHECKER
score = int(input("Please enter a score to see if you have passed: "))

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else:
    print("You got an F")




#WEATHER ADVISE

weather = input("Enter a weather subscrption, you can chooes from: sunny, rain, wind, storm and fogg and get advise: ")
if weather == "sunny":
    print("Use suntan!")
elif weather == "rain":
    print("Bring an umbrella!")
elif weather == "wind":
    print("Don´t loose your hat!")
elif weather == "storm":
    print("Hold on tight!")
elif weather == "fogg": 
    print("Be careful!")
else:
    print("Sorry your input wasn´t recognized")
    
