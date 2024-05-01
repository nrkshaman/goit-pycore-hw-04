from task1.main import read_data

def get_cats_info(path:str) -> list[dict[str, str]]:
    cats = read_data(path)
    cats_info = list()
    for cat in cats:
        id, name, age = cat.split(",")
        cats_info.append({"id": id, "name": name, "age": age})
    return cats_info

def main():
    print(get_cats_info("test.txt"))

if __name__ == "__main__":
    main()
