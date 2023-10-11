def draw_modular_rectangle(width, height):  #defining a function that holds 2 arguments
    for a in range(height):  #a represents row and b represents column
        for b in range(width):
            print((a * width + b) % 10, end=" ")  #"% 10" ensures the results stay in the range 0 to 9 and #"end= " " " ensures whitespaces
        print()

#get user input
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

#draw the rectangle
draw_modular_rectangle(width, height)
