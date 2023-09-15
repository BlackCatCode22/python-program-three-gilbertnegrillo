# python_program_three.py

# Gilbert Negrillo
# CIT-95
# September 12 2023

contacts = [] # Created an empty list called contacts.

contact1 = {"name": "Gilbert Negrillo", "phone": "559-284-1234", "email": "bertnegrillo@gmail.com"} # Each contact is represented as a dictionary with the keys: name, phone, email.
for key, value in contact1.items():
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

def add_contact(): # Implemented a function called add_contact.
    name = input("Enter a name: ") # Input user's name
    if any(contact["name"] == name for contact in contacts): # Create if-else statement to make sure contact name is unique.
        print("That name already exists in the contact.")
    else:
        phone = input("Enter a phone number: ")
        email = input("Enter an email address: ")
        new_contact = {"name": name, "phone": phone, "email": email}
        for key, value in new_contact.items():
            print(f"{key}: {value}")
        contacts.append(new_contact) # Use append method to add to contacts list.
        print("New contact added.")

add_contact() # Call add_contact function.
print(contacts)


