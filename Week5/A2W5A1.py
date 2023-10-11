import os
import sys


valid_lines = []
corrupt_lines = []


def validate_data(line):
    student_number, first_name, last_name, dob, program = line.strip().split(',')

    first_name = first_name.title()
    last_name = last_name.title()
    program = program.upper()

    if not (student_number.startswith('08') or student_number.startswith('09')):
        corrupt_lines.append(f'{line} => INVALID DATA: Student number is invalid.')

    if any(not c.isalpha() and c != '_' for c in last_name):
        corrupt_lines.append(f'{line} => INVALID DATA: Last name contains special characters.')

    if program not in ['INF', 'TINF', 'CMD', 'AI']:
        corrupt_lines.append(f'{line} => INVALID DATA: Invalid program.')

    if not is_valid_date_of_birth(dob):
        corrupt_lines.append(f'{line} => INVALID DATA: Invalid date of birth.')

    if all((student_number.startswith('08') or student_number.startswith('09'),
            all(c.isalpha() or c == ' ' for c in first_name),
            all(c.isalpha() or c == ' ' for c in last_name),
            is_valid_date_of_birth(dob),
            program in ['INF', 'TINF', 'CMD', 'AI'])):
        valid_lines.append(line)


def is_valid_date_of_birth(dob):
    try:
        year, month, day = map(int, dob.split('-'))
        return 1960 <= year <= 2004 and 1 <= month <= 12 and 1 <= day <= 31
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


if __name__ == "__main__":
    main('students.csv')
