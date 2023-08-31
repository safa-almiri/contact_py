
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                break

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found")
        else:
            for contact in self.contacts:
                print(contact)
                print("--------------------")

contact_manager = ContactManager()

while True:
    print("1. Add contact")
    print("2. Remove contact")
    print("3. Search contact")
    print("4. Display contacts")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact = Contact(name, phone, email)
        contact_manager.add_contact(contact)
        print("Contact added successfully")
    elif choice == "2":
        name = input("Enter name: ")
        contact_manager.remove_contact(name)
        print("Contact removed successfully")
    elif choice == "3":
        name = input("Enter name: ")
        contact = contact_manager.search_contact(name)
        if contact:
            print(contact)
        else:
            print("Contact not found")
    elif choice == "4":
        contact_manager.display_contacts()
    else:
        break

