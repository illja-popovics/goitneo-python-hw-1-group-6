def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def phone_contact(args, contacts):
    if len(args) == 1:
        phone = args[0]
        if phone in contacts:
            print(contacts[phone])
        else:
            print("Contact not found.")
    else:
        print("Invalid input. Please provide a name.")

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid input. Please provide a name and a phone number."

def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid input. Please provide a name and a new phone number."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            show_all(contacts)
        elif command == "help":
            print("Available commands: add, change, phone, all, help, close, exit")
        elif command == "phone":
            phone_contact(args, contacts)
        else:
            print("Invalid command.")



print(main)


if __name__ == "__main__":
    main()