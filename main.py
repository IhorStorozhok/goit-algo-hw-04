def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def show_contacts(contacts):
    print(contacts)

def show_phone(args, contacts):
    name = args[0]
    print(contacts.get(name, "Contact not found."))
      

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        command = command.strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            show_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()