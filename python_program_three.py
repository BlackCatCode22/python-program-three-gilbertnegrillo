# python_program_three.py

# Gilbert Negrillo
# CIT-95
# September 12 2023

contacts = []  # Created an empty list called contacts.

contact1 = {"name": "Gilbert Negrillo", "phone": "559-284-1234", "email": "bertnegrillo@gmail.com"}  # Each contact
# is represented as a dictionary with the keys: name, phone, email.
for key, value in contact1.items():  # Used items method to return the list with all dict. keys with values.
    print(f"{key}: {value}")
print("\n\n")
contacts.append(contact1)
print("\n")
print(contacts)

contact2 = {"name": "Donald Duck", "phone": "559-308-4321", "email": "donduck@gmail.com"}
for key, value in contact2.items():
    print(f"{key}: {value}")
print("\n\n")
contacts.append(contact2)
print("\n")
print(contacts)

contact3 = {"name": "Minnie Mouse", "phone": "559-638-7231", "email": "minniem@gmail.com"}
for key, value in contact3.items():
    print(f"{key}: {value}")
print("\n\n")
contacts.append(contact3)
print("\n")
print(contacts)


def add_contact():  # Implemented a function called add_contact.
    name = input("\nEnter a name: ")  # Takes user's input to enter a contact name.
    if any(contact["name"] == name for contact in contacts):  # Create if-else statement to make sure contact name is
        # unique.
        print("That name already exists in the contact.")  # Message showing user that the name already exists in the
        # contacts list.
    else:
        phone = input("Enter a phone number: ")  # Take user's input to enter a phone number.
        email = input("Enter an email address: ")  # Take user's input to enter an email address.
        new_contact = {"name": name, "phone": phone, "email": email}  # Create new dictionary.
        for key, value in new_contact.items():  # Iterate through key-value pairs.
            print(f"{key}: {value}")  # Use f functon to format Print key-value pairs.
        contacts.append(new_contact)  # Use append method to add to contacts list.
        print("New contact added.")  # Verify contact has been added.


add_contact()  # Call add_contact function.


def view_contacts():  # Implemented a function called view_contacts.
    print("\nList of all Contacts:")
    for contact in contacts:  # Use for/in loop to iterate through the contacts list.
        for key, value in contact.items():  # Iterate through key-value pairs
            print(f"{key}: {value}")
        print()


view_contacts()   # Call view_contacts function.


def search_contact():  # Implemented search_contact function.
    name = input("\nSearch a contact name: ")  # Takes user input to search for contact name.
    for contact in contacts:  # Use for/in loop to iterate through contacts list
        if contact["name"] == name:  # Use if/else statement.
            for key, value in contact.items():  # If name is found in the contacts list, use for/in loop to iterate
                # through key-value pairs
                print(f"{key} : {value}")
            break
    else:
        print("That name does not exist in the contacts list.")  # Message showing contact was not found.


search_contact()  # Call search_contact function.
