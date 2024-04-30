from colorama import Fore
TAB = "|   "
TAB_EL = "|-- "
TAB_LAST_EL = "`-- "

def print_dir(dir_name:str, tabs:int, last:bool):
    coloprint(dir_name, tabs, last, Fore.BLUE)

def print_file(file_name:str, tabs:int, last:bool):
    coloprint(file_name, tabs, last, Fore.GREEN)

def coloprint(str:str, tabs:int, last:bool, colour:str):
    tab=TAB*(tabs-1)
    if last:
        tab+=TAB_LAST_EL
    elif tabs>0:
        tab+=TAB_EL
    print(tab + colour + str + Fore.RESET)

def print_error(str:str):
    print(Fore.RED + "[ERROR] " + Fore.RESET + str)

def main():
    print_dir("Directory", 0, False)
    print_file("File", 1, False)
    print_dir("Directory", 1, True)
    print_dir("Directory", 2, True)
    print_dir("Directory", 3, False)
    print_file("File", 3, True)

if __name__ == "__main__":
    main()