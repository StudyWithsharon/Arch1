def is_black_square(row, column):
    #define a dictionary to map letters to numbers
    column_index = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    #check if the column is a valid key in the dictionary
    if column in column_index:
        column_number = column_index[column]

        #determine if the square is black or white based on row and column
        if (row + column_number) % 2 == 0:
            return True
        else:
            return False
    else:
        print(f"Invalid column: {column}. Please enter a valid column (a-h).")

#prompt the user for input
position = input("Enter a chessboard position (e.g., 'a1'): ")
column = position[0].lower()  # Extract the column letter and convert to lowercase
row = int(position[1])

#check if the square is black or white
if is_black_square(row, column):
    print("black|zwart")
else:
    print("white|wit")
