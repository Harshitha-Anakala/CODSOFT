class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_from_file()

    def add_contact(self, name, phone_number, email):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully!\n")

    def view_contact_list(self):
        if not self.contacts:
            print("Contact book is empty.\n")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone_number']}")
            print()

    def search_contact(self, search_query):
        results = []
        for contact in self.contacts:
            if (
                search_query.lower() in contact['name'].lower() or
                search_query in contact['phone_number']
            ):
                results.append(contact)
        return results

    def update_contact(self, contact_index, new_phone_number, new_email):
        contact = self.contacts[contact_index]
        contact['phone_number'] = new_phone_number
        contact['email'] = new_email
        print("Contact updated successfully!\n")

    def delete_contact(self, contact_index):
        deleted_contact = self.contacts.pop(contact_index)
        print(f"Contact '{deleted_contact['name']}' deleted successfully!\n")

    def save_to_file(self, filename='contacts.txt'):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                line = f"{contact['name']},{contact['phone_number']},{contact['email']}\n"
                file.write(line)

    def load_from_file(self, filename='contacts.txt'):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, phone_number, email = line.strip().split(',', 2)
                    self.contacts.append({
                        'name': name,
                        'phone_number': phone_number,
                        'email': email
                    })
        except FileNotFoundError:
            pass 
def main():
    contact_book = ContactBook()

    while True:
        print("CONTACT BOOK")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_book.add_contact(name, phone_number, email)

        elif choice == '2':
            contact_book.view_contact_list()

        elif choice == '3':
            search_query = input("Enter contact name or phone number to search: ")
            results = contact_book.search_contact(search_query)
            if results:
                print("Search Results:")
                for contact in results:
                    print(f"{contact['name']} - {contact['phone_number']} - {contact['email']}")
                print()
            else:
                print("No matching contacts found.\n")

        elif choice == '4':
            contact_book.view_contact_list()
            contact_index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= contact_index < len(contact_book.contacts):
                new_phone_number = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
                contact_book.update_contact(contact_index, new_phone_number, new_email)
            else:
                print("Invalid contact number.\n")

        elif choice == '5':
            contact_book.view_contact_list()
            contact_index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= contact_index < len(contact_book.contacts):
                contact_book.delete_contact(contact_index)
            else:
                print("Invalid contact number.\n")

        elif choice == '6':
            contact_book.save_to_file()
            print("Contact book saved to 'contacts.txt'. Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
