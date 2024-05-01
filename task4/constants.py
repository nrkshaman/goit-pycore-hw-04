from colorama import Fore


BANNER = """
   _                                       
  /   _  ._  _|_  _.  _ _|_  _   |_   _ _|_ 
  \\_ (_) | |  |_ (_| (_  |_ _>   |_) (_) |_ 
"""
GREETING = """Hi! I am your bot-helper! I will help you to manage your contacts list.
Enter `help` for more information"""
INSTRUCTIONS = """hello                        : responds "How can I help you?" in console
add [username] [phone]       : saves new contact
change [username] [phone]    : updates existing phone number
phone [username]             : prints phone number for username
all                          : prints all saved contacts
close, exit                  : prints "Good bye!" and finishes bot
help                         : prints this help"""
INFO = Fore.GREEN + "[INFO]" + Fore.RESET
ERROR = Fore.RED + "[ERROR]" + Fore.RESET
INVALID_COMMAND = ERROR + " Invalid command. Please use 'help'"