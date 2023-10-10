#we define a function that takes 3 arguments a, b and c, with does 3 arguments this function can determine what type of triangle it is
def classify_triangle(a, b, c):
    if a == b == c: #using basic operators to check if all sides are equal
        return "equilateral"
    elif a == b or b == c or a == c: #this line checks if at least 2 sides are equal
        return "isosceles"
    else: #when all sides are different
        return "scalene"

def main():
    try: #this will handle errors, we ask user to input in a certain format
        input_user = input("Enter the sides of the triangle in this format a=1, b=2, c=3: ")
        sides = [int(side.split('=')[1]) for side in input_user.split(', ')] #now we have all the input in one string we need to split this up in 3 items and we just want to save the number or actual value
        #so to be clear we first split letter from number by "=" and index offset 1 and we split the numbers by ", "
        if len(sides) == 3: #checks if user put in 3 sides like we asked
            side1, side2, side3 = sides[0], sides[1], sides[2]
            triangle_type = classify_triangle(side1, side2, side3)
            print(f"The triangle is classified as: {triangle_type}")
        else:
            print("Please provide exactly three sides.")
    except ValueError:
        print("Invalid input. Please enter three sides in the format a=1, b=2, c=3.")

if __name__ == "__main__":
    main()
