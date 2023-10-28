import os #provides functions to interact with the operating system
import sys #provides access to interpreter-related variables and functions
import json #allows encoding and decoding of JSON data


'''
print all contacts in the following format:
======================================
Position: <position>
First name: <firstname>
Last name: <lastname>
Emails: <email_1>, <email_2>
Phone numbers: <number_1>, <number_2>
'''
def display(addressbook: list):
    for contact in addressbook: #this function takes a list called adressbook as an argument and iterates trough each contact
        print("======================================")
        print(f"Position: {contact['id']}")
        print(f"First name: {contact['first_name']}")
        print(f"Last name: {contact['last_name']}")
        print(f"Emails: {', '.join(contact['emails'])}")
        print(f"Phone numbers: {', '.join(contact['phone_numbers'])}")

'''
return list of contacts sorted by first_name or last_name [if blank then unsorted], direction [ASC (default)/DESC])
'''
def list_contacts(addressbook, sort_by="first_name", direction="ASC"): #this function takes the adressbook list and 2 optianl paramters. It will sort the list
    sorted_contacts = sorted(addressbook, key=lambda x: x[sort_by], reverse=(direction == "DESC"))
    return sorted_contacts

'''
add new contact:
- first_name
- last_name
- emails = {}
- phone_numbers = {}
'''
def add_contact(addressbook, first_name, last_name, emails, phone_numbers): #this function adds new contacts and gives them a unique ID number
    new_id = max([c["id"] for c in addressbook], default=0) + 1 #using a for loop to get tha max ID number and than adding +1 to the new contact, when no contacts it defaults to 0 adding 1
    new_contact = { #creates a new contact storing the info in a dictionary
        "id": new_id,
        "first_name": first_name,
        "last_name": last_name,
        "emails": emails,
        "phone_numbers": phone_numbers
    }
    addressbook.append(new_contact)
    return addressbook

'''
remove contact by ID (integer)
'''
def remove_contact(addressbook, contact_id):
    addressbook = [contact for contact in addressbook if contact["id"] != contact_id]
    return addressbook


'''
merge duplicates (automated > same fullname [firstname & lastname])
'''
def merge_contacts(addressbook):
    full_names = set((contact["first_name"] + contact["last_name"]).lower() for contact in addressbook)
    for full_name in full_names:
        duplicates = [contact for contact in addressbook if (contact["first_name"] + contact["last_name"]).lower() == full_name]
        if len(duplicates) > 1:
            main_contact = duplicates.pop(0)
            for duplicate in duplicates:
                main_contact["emails"].extend(duplicate["emails"])
                main_contact["phone_numbers"].extend(duplicate["phone_numbers"])
                addressbook.remove(duplicate)
    return addressbook

'''
read_from_json
Do NOT change this function
'''
def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            contact['id'] = int(contact['id'])
            addressbook.append(contact)

    return addressbook


'''
write_to_json
Do NOT change this function
'''
def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent = 4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


'''
main function:
# build menu structure as following
# the input can be case-insensitive (so E and e are valid inputs)
# [L] List contacts
# [A] Add contact
# [R] Remove contact
# [M] Merge contacts
# [Q] Quit program
Don't forget to put the contacts.json file in the same location as this file!
'''
def main(json_file):
    addressbook = read_from_json(json_file)

    while True:
        print("[L] List contacts")
        print("[A] Add contact")
        print("[R] Remove contact")
        print("[M] Merge contacts")
        print("[Q] Quit program")

        choice = input("Enter your choice: ").upper()

        if choice == "L":
            display(addressbook)

        elif choice == "A":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            emails = input("Enter emails (comma separated): ").split(", ")
            phone_numbers = input("Enter phone numbers (comma separated): ").split(", ")

            addressbook = add_contact(addressbook, first_name, last_name, emails, phone_numbers)

        elif choice == "R":
            contact_id = int(input("Enter contact ID to remove: "))
            addressbook = remove_contact(addressbook, contact_id)

        elif choice == "M":
            addressbook = merge_contacts(addressbook)

        elif choice == "Q":
            write_to_json(json_file, addressbook)
            break

        else:
            print("Invalid choice. Please try again.")

'''
calling main function: 
Do NOT change it.
'''
if __name__ == "__main__":
    main('contacts.json')
