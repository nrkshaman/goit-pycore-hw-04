
def read_data(path:str) -> list[str] | None:
    try:
        with open(path, "r", encoding="UTF-8") as salaries_file:
            salaries = list()
            for line in salaries_file.readlines():
                salaries.append(line.strip())
            return salaries
    except FileNotFoundError as fnf:
        print(fnf)
        print("File was not found")
        return None
    except ValueError as ve:
        print(ve)
        print("Incorrect data in the file")
        return None

def process_salaries(dev_salaries:list[str]) -> tuple[int, int] | tuple[None, None]:
    salaries=list()
    for dev_salary in dev_salaries:
        _, salary = dev_salary.split(",")
        salary = int(salary)
        salaries.append(salary)
    if salaries:
        total_sum = sum(salaries)
        avg = total_sum/len(salaries)
        return (total_sum, avg)
    else:
        return (None, None)

def total_salary(path:str) -> tuple[int, int]:
    return process_salaries(read_data(path))


def main():
    total, average = total_salary("test.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()