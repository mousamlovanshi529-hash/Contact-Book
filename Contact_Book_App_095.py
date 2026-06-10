# Program to create a Contact Book

Contacts = {}

while True:
    print("\n**** Contact Book App ****")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = int(input("Enter the number between 1-7 to perform an operation: "))

    # Create Contact
    if choice == 1:
        name = input("Enter your name: ")

        if name in Contacts:
            print(f"Contact name {name} already exists!!")
        else:
            age = int(input("Enter the age: "))
            email = input("Enter the email: ")
            mobile = int(input("Enter the mobile number: "))

            Contacts[name] = {
                "age": age,
                "email": email,
                "mobile": mobile
            }

            print(f"Contact name {name} has been created successfully.")

    # View Contact
    elif choice == 2:
        name = input("Enter contact name to view: ")

        if name in Contacts:
            contact = Contacts[name]

            print(f"Name: {name}")
            print(f"Age: {contact['age']}")
            print(f"Email: {contact['email']}")
            print(f"Mobile Number: {contact['mobile']}")
        else:
            print("!! Contact not found !!")

    # Update Contact
    elif choice == 3:
        name = input("Enter name to update contact: ")

        if name in Contacts:
            age = int(input("Enter updated age: "))
            email = input("Enter updated email: ")
            mobile = int(input("Enter updated mobile number: "))

            Contacts[name] = {
                "age": age,
                "email": email,
                "mobile": mobile
            }

            print("Contact updated successfully.")
        else:
            print("Contact not found!!")

    # Delete Contact
    elif choice == 4:
        name = input("Enter name to delete: ")

        if name in Contacts:
            del Contacts[name]
            print(f"Contact name {name} has been deleted successfully.")
        else:
            print("!! Contact not found !!")

    # Search Contact
    elif choice == 5:
        search_name = input("Enter contact name to search: ")

        found = False

        for name, contact in Contacts.items():
            if search_name.lower() in name.lower():
                print(
                    f"Found - Name: {name}, "
                    f"Age: {contact['age']}, "
                    f"Email: {contact['email']}, "
                    f"Mobile Number: {contact['mobile']}"
                )
                found = True

        if not found:
            print("No contact found with that name!!")

    # Count Contact
    elif choice == 6:
        print(f"Total contacts in your book: {len(Contacts)}")

    # Exit
    elif choice == 7:
        print("Good Bye... Closing the program.")
        break
        
    else:
        print("!! Invalid input !! Please try again.")