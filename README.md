[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/07tV9k7q)
# tPythonListsAndDicts01
Python List and Dictionary Program

Use the attached sample code to help with Python Program Three - Lists and Dictionaries

More sample code will be pushed to this template repo throughout the week as students ask for help.

Python Program Three - Exploring Python Data Structures with Lists and Dictionaries

Course: Python Programming (CIT-95)
Professor: Dennis Mohle
Fresno City College, Fresno, California

Description:

In this assignment, you will continue to build your Python programming skills by exploring and manipulating various Python data structures, including lists, strings, and dictionaries. You have been learning Python for five weeks, and this assignment will challenge you to apply your knowledge effectively. The goal is to reinforce your understanding of Python data structures and how to create user-defined methods to solve real-world problems.

Deliverables:

Python Program Three Script: A well-documented Python script named "python_program_three.py" that contains your code for this assignment.

ReadMe on GitHub Classroom: Use the ReadMe file in your GitHub Classroom remote repository to summarize your program, its functionality, and the approach you took to solve the problem. 

Verbose Comments: Explain and comment each section of your code. Explain your thought process, reasoning, and any assumptions made during the implementation.

Testing Results in ReadMe: In the same ReadMe file on GitHub Classroom, include a section where you describe the test cases you created to ensure the correctness of your program. List the test cases and their outcomes. Explain how your program handles different scenarios and any improvements you would make if you had more time.

Assignment Details:
You are tasked with developing a Python program that simulates a basic contact management system. Your program should allow users to add, view, and search for contacts. Each contact will have a name, phone number, and email address. You will use Python lists, strings, and dictionaries to implement this system.

Requirements:

Create an empty list called contacts to store contact information. Each contact should be represented as a dictionary with the following keys:

'name': The name of the contact (a string).
'phone': The phone number of the contact (a string).
'email': The email address of the contact (a string).

Implement a function called add_contact() that takes user input to add a new contact to the contacts list. Ensure that each contact has a unique name.

Implement a function called view_contacts() that displays the list of all contacts in a user-friendly format.

Implement a function called search_contact() that takes a name as input and searches for the contact by name. If found, display the contact's details. If not found, display a message indicating that the contact was not found.

Use string formatting and string methods (e.g., format(), split(), strip(), etc.) to format and validate user input as necessary.

Additional Guidelines:

Basic: Make sure to create user-defined methods for adding, viewing, and searching for contacts.

Basic: Commit to your GitHub Classroom repo whenever you create a program update. This shows me that you're working and learning, and also earns you commits on your GitHub profile!

Advanced: Your program will provide a menu with options to add a contact, view all contacts, search for a contact, and exit the program.

Advanced: Implement error handling to handle invalid user input.

Advanced: Use Python file i/o to output your list of contacts to a text file on your local machine. 

Submission:

Submit your "python_program_three.py" program and update the ReadMe.md file in your GitHub Classroom remote repository by the specified deadline.

Grading Criteria:

You will be assessed based on the following criteria:

Correctness of the program's functionality.
Proper use of Python data structures (lists, dictionaries, strings).
Clarity and organization of your code.
Comprehensive and well-structured summary of your program in the ReadMe.md file.
Adherence to Python coding conventions and best practices.

Good luck, and enjoy working on this assignment! If you have any questions or need clarification, reach out during weekend office hours or via the Canvas inBox.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Test Case - Line 35: To make sure the user input's a unique contact name that does not exist in the contacts list, I used any function to check if the name entered is equal to the names for contact in contacts list. I added the any function because if I didn't then any input the user would have entered it would have said that the name already exists even if the name did not exist in the contacts list.
Test Case - Line 35-48: If I had more time, an improvement I would have tried to make is allow the user to input a name again instead of terminating the program if the name they typed had already existed in the contacts list.
Test Case - If I had more time, I would have liked to try and create a menu with options to add a contact, view all contacts, search for a contact, or exit the program.
Test Case - Handling errors and validating user input is also something I should have done more if I had more time.

Summary:
The first thing I did was create my contacts variable and with an empty list. In lines 9-32 are each contact is represented as a dictionary with the keys: name, phone, and email. 
To get the key-value pairs, I used a for/in loop in each contact with the items method to return the list with all dictionary keys with values. 
Throughout the code, I used the f function to format the key-value pairs. 
The first function in the program is add_contact, which has no parameters and takes no arguments to the function call. This is where it takes user input and add a new contact to the contacts list. To make sure each contact has a unique name I used an if-else statement. If the user enters a name that already exists in the contacts list then it will print the message to the user saying that the name already exists in the contacts list. Else, the user will be able to add a new contact if the name that was entered did not exist in the contacts lists. I used the append method to add the new contact to the contacts list.
The second function in the program is view_contacts, which has no parameters and takes no arguments to the function call. This displays the list of all contacts. I used the for/in loop to iterate through the contacts list. Then I used a for/in loop to iterate through key-value pairs. To put it in a user-friendly format, I used the f function to format the key-value pairs.
The last function in the program is search_contact, which has no parameters and takes no arguments to the function call. This takes a name as input and searches for the contact by name. I used a for/in loop to iterate through the contacts list. Then I used an if-else statement. If the user entered a name that was in the contacts list then it would display the contact's details. Else, a message will be printed indicating that the contact was not found.


