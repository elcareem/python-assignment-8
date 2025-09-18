"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_no):
        if name in self.contacts:
            if phone_no not in self.contacts.values():
                if not isinstance(self.contacts[name], list):
                    self.contacts[name] = [self.contacts[name]]
                self.contacts[name].append(phone_no)
            return "Contact already exist"        
        for contact_name, contact_no in self.contacts.items():
            if contact_no == phone_no:
                return f"Contact already saved with name {contact_name}"

        self.contacts.update({name: phone_no})

    def delete_contact(self, name):
        if name not in self.contacts:
            return "Contact doesn't exist"
        self.contacts.pop(name)
    
    def search_contact(self, name):
        if name not in self.contacts:
            return "Contact doesn't exist"
        return self.contacts[name]

    def show_contacts(self):
        return self.contacts

book = ContactBook()
book.add_contact("Alice", "08012345678")
print(book.add_contact("Alice", "08012345679"))
print(book.add_contact("Jane", "08012345648"))
print(book.add_contact("Alice", "08012345674"))
print(book.search_contact("Alice"))

print(book.show_contacts())
