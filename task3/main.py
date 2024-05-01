from pathlib import Path
from sys import argv
from nice_print import print_dir, print_file, print_error

def traverse_dir(path:Path, tabs=1):
    tree = list(path.iterdir())
    last=False
    for i, node in enumerate(tree):
        if i == len(tree)-1:
            last=True
        if node.is_dir():
            print_dir(node.name, tabs, last)
            traverse_dir(node, tabs+1)
        else:
            print_file(node.name, tabs, last)

def main():
    if len(argv) < 2:
        print_error("Please provide path to the directory you wish to traverse")
        return
    path = Path(argv[1])
    if not path.is_dir():
        print_error("Provided path has to point to the directory")
        return
    print_dir(path.name, 0, False)
    traverse_dir(path)

if __name__ == "__main__":
    main()
