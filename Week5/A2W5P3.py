def check_triangle(a, b, c):  #defined a function that takes 3 arguments
    if a >= b + c or b >= a + c or c >= a + b: #check if sides can form a triangle
        return False
    return True

if __name__ == "__main__":
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input("Enter the length of side B: "))
    side_c = float(input("Enter the length of side C: "))

    if check_triangle(side_a, side_b, side_c):
        print("Possible")
    else:
        print("Impossible")
