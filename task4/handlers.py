from constants import *

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
    all = f"{'Name':<15}{'| Phone'}\n" + "-"*32 + "\n"
    for name in contacts:
        all += f"{name: <15}| {contacts[name]}\n"
    return all.strip()