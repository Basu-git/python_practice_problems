# Add contact (name, phone) ○ Search contact
# 
# 
# 
# by name ○ Delete contact ○ Show all conta
contact={}
def add_contact(name,phone):
    contact[name]=phone
    print(f"{contact} added successfully")
def search(name):
    if name in contact:
        print(f"{name}:{contact[name]}")
    else:
        print(f"{name} is not found")
def delete(name):
    if name in contact:
        del contact[name]
        print(contact)
    else:
        print("Such results are not found to delete")
        
def all_contact():
    if contact:
        print("All Contacts\n")
        for name,phone in contact.items():
            print(f"{name}:{phone}")
    else:
        print("No contacts")
def menu():
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts")
        print("5. Exit")
menu()
while True:
    choice=input("Enter your choice(1-5): ")
    if choice=="1":
        name=input("Enter your name: ")
        phone=int(input("Enter your phone number: "))
        add_contact(name,phone)
    elif choice=="2":
        name=input("Enter your name: ")
        search(name)
    elif choice=="3":
        name=input("Enter your name: ")
        delete(name)
    elif choice=="4":
        all_contact()
    elif choice=="5":
        print("Exiting the contact book")
        break
    else:
        print("INVALID CHOICE<plx try againn")
    menu()
all_contact()
