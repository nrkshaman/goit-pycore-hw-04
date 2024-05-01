from colorama import Fore

BANNER = """
   _                                       
  /   _  ._ _|_  _.  _ _|_  _   |_   _ _|_ 
  \_ (_) | | |_ (_| (_  |_ _>   |_) (_) |_ 
"""
GREETING = """Hi! I am your bot-helper! I will help you to manage your contacts list.
Enter `help` for more information"""
INSTRUCTIONS = """hello : responds "How can I help you?" in console
add [username] [phone] : saves new contact
change [username] [phone] : updates existing phone number
phone [username] : prints phone number for username
all : prints all saved contacts
close | exit : prints "Good bye!" and finishes bot
help : prints this help"""
INFO = Fore.GREEN + "[INFO]" + Fore.RESET
ERROR = Fore.RED + "[ERROR]" + Fore.RESET
INVALID_COMMAND = ERROR + " Invalid command. Please use 'help'"


def parse_input(user_input: str):
    try:
        cmd, *args = user_input.split()
    except ValueError:
        return INVALID_COMMAND
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args:list[str], contacts:dict[str, str]) -> str:
    try:
        name, phone, = args
    except ValueError:
        return INVALID_COMMAND
    if name not in contacts:
        contacts[name] = phone
        return INFO + f" Contact {name} successfully added."
    else:
        return ERROR + " Contact already exists."

def change_contact(args:list[str], contacts:dict[str, str]) -> str:
    try:
        name, phone, = args
    except ValueError:
        return INVALID_COMMAND
    if name in contacts:
        contacts[name] = phone
        return INFO + f" Contact {name} successfully changed."
    else:
        return ERROR + " Contact does not exist."
    
def phone_contact(args:list[str], contacts:dict[str, str]) -> str:
    try:
        name, = args
    except ValueError:
        return INVALID_COMMAND
    if name in contacts:
        return contacts[name]
    else:
        return ERROR + " Contact does not exist."

def all_contact(contacts:dict[str, str]) -> str:
    all = ""
    for name in contacts:
        all += f"Name: {name} Phone: {contacts[name]}\n"
    return all.strip()

def main():
    contacts = {}
    print(BANNER)
    print(GREETING)
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
        elif command == "all":
            print(all_contact(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone_contact(args, contacts))
        elif command == "help":
            print(INSTRUCTIONS)
        else:
            print(INVALID_COMMAND)

if __name__ == "__main__":
    main()