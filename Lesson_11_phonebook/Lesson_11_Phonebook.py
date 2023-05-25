# Task 1

with open('myfile.txt', 'w') as file:
    file.write('Hello file world!\n')

with open('myfile.txt', 'r') as file:
    print(file.read())

# Якщо файл з таким шляхом існує, то він буде відкритий і
# прочитаний або перезаписаний залежно від режиму відкриття.

# Task 2

import json
import sys


def load_phonebook(file_name):
    try:
        with open(file_name, 'r') as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        phonebook = {}
    return phonebook


def save_phonebook(phonebook, file_name):
    with open(file_name, 'w') as file:
        json.dump(phonebook, file)


def print_contact(contact):
    # print("Phone Number:", contact)
    print("First Name:", contact["first_name"])
    print("Last Name:", contact["last_name"])
    print("Full Name:", contact["full_name"])
    print("City:", contact["city"])
    print()


def add_contact(phonebook):
    phone_number = input("Enter phone number: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + " " + last_name
    city = input("Enter city: ")

    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "city": city
    }

    phonebook[phone_number] = contact
    print("Contact added successfully.")


def search_contact(phonebook):
    search_term = input("Enter search term: ").lower()

    found_contacts = []
    for phone_number, contact in phonebook.items():
        contact_values = [value.lower() for value in contact.values()]
        if any(search_term in value for value in contact_values) or search_term == phone_number:
            found_contacts.append((phone_number, contact))

    if found_contacts:
        print("Search Results:")
        for phone_number, contact in found_contacts:
            print("Phone Number:", phone_number)
            print_contact(contact)
    else:
        print("No contacts found.")


def del_contact(phonebook):
    phone_number = input("Enter phone number: ")

    if phone_number in phonebook:
        contact = phonebook.pop(phone_number)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def change_contact(phonebook):
    phone_number = input("Enter phone number: ")

    if phone_number in phonebook:
        contact = phonebook[phone_number]

        first_name = input("Enter new first name: ")
        last_name = input("Enter new last name: ")
        full_name = input("Enter new full name: ")
        city = input("Enter new city: ")

        contact["first_name"] = first_name
        contact["last_name"] = last_name
        contact["full_name"] = full_name
        contact["city"] = city

        print("Contact changed successfully.")
    else:
        print("Contact not found.")


def exit_program(phonebook, file_name):
    save_phonebook(phonebook, file_name)
    print("Phonebook saved successfully.")
    sys.exit()


def start():
    file_name = input("Input the Phonebook name: ")
    phonebook = load_phonebook(file_name)
    while True:
        print()
        print("Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Change Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            del_contact(phonebook)
        elif choice == "4":
            change_contact(phonebook)
        elif choice == "5":
            exit_program(phonebook, file_name)
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    print(sys.argv[0])
    start()
