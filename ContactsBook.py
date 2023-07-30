import os 
cf ="contacts.txt"
def load_contacts():
    contacts={}
    if os.path.exists(cf):
        with open(cf,"r") as FILE: 
            for line in FILE :
                name,phone= line.strip().split(":")
                contacts[name]=phone
    return contacts
def add_contacts(contacts):
    name=input("Enter the contact's name: ")
    phone=input("Enter the respective contact's phone number: ")
    contacts[name]=phone
    print("Contact added successfully! ")
def view_contact(contacts):
    if contacts:
        for name,phone in contacts.items():
            print(f"{name}: {phone} ")
    else:
        print("Contact book is empty.")
def search_contact(contacts):
    name=input("Enter the contact's name to search.")
    phone=contacts.get(name)
    if phone:
        print(f"{name}: {phone} ")
    else:
        print("contact not found")
def save_contacts(contacts):
    with open(cf,"w") as FILE: 
        for name,phone in contacts.items():
            FILE.write(f"{name}: {phone}\n")

def main():
    contacts=load_contacts()
    while True:
        print ("Contact Book Menu.")
        print("1. View Contacts.")
        print("2. Add Contacts.")
        print("3. Search Contacts.")
        print("Exit")
        choice=input("Enter your choice; 1,2,3,4: ")
        if choice=="1":
            view_contact(contacts)
        elif choice=="2":
            add_contacts(contacts)
        elif choice=="3":
            search_contact(contacts)
        elif choice=="4":
            save_contacts(contacts)
            print("Exiting contacts book.")
            break
        else:
            print("Invalid choice.")
if __name__=="__main__":
    main()

