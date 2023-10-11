import os #provides ways to interact with the operating system
import sys #predefined variables

#empty lists to store valid and corrupt lines
valid_lines = []
corrupt_lines = []

#this functions takes one argument, this function will check each line
def validate_data(line):
    student_number, first_name, last_name, dob, program = line.strip().split(',') #using strip to remove whitespaces and split by ","

    first_name = first_name.title() #using title to have the name start with a cap. letter
    last_name = last_name.title()
    program = program.upper() #using upper to have all caps

    if not (student_number.startswith('08') or student_number.startswith('09')): #checks if student number start with "08" or "09"
        corrupt_lines.append(f'{line} => INVALID DATA: Student number is invalid.')

    if any(not c.isalpha() and c != '_' for c in last_name): #checks for alphabetical letters and underscores
        corrupt_lines.append(f'{line} => INVALID DATA: Last name contains special characters.') #adds it to our list corrupt_lines

    if program not in ['INF', 'TINF', 'CMD', 'AI']: #checks if program is one of the specified options
        corrupt_lines.append(f'{line} => INVALID DATA: Invalid program.') #adds invalid line to the corrupt list

    if not is_valid_date_of_birth(dob):
        corrupt_lines.append(f'{line} => INVALID DATA: Invalid date of birth.')

    if all((student_number.startswith('08') or student_number.startswith('09'), #when line passes all the checks it is added to valid list
            all(c.isalpha() or c == ' ' for c in first_name),
            all(c.isalpha() or c == ' ' for c in last_name),
            is_valid_date_of_birth(dob),
            program in ['INF', 'TINF', 'CMD', 'AI'])):
        valid_lines.append(line) #adds it the list valid_lines


def is_valid_date_of_birth(dob):
    try:
        year, month, day = map(int, dob.split('-')) #map takes each item and applies it to the function, turns input to int, splits is by "-" 
        return 1960 <= year <= 2004 and 1 <= month <= 12 and 1 <= day <= 31 #checks date input if it is within the boundries
    except ValueError:
        return False


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        next(csv_file)

        for line in csv_file:
            validate_data(line)

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":  #makes sure code is run directly
    main('students.csv')
