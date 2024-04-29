

def read_salaries(path:str) -> list[float] | None:
    try:

        with open(path, "r", encoding="UTF-8") as salaries_file:
            salaries = list()
            for line in salaries_file.readlines():
                _, salary = line.strip().split(",")
                salary = int(salary)
                salaries.append((salary))
            return salaries
    except FileNotFoundError as fnf:
        print(fnf)
        print("File was not found")
        return None
    except ValueError as ve:
        print(ve)
        print("Incorrect data in the file")
        return None

def get_total_and_avg(data:list[int]) -> tuple[int, int] | tuple[None, None]:
    if data:
        total_sum = sum(data)
        avg = total_sum/len(data)
        return (total_sum, avg)
    else:
        return (None, None)

def total_salary(path:str) -> tuple[int, int]:
    return get_total_and_avg(read_salaries(path))


def main():
    total, average = total_salary("task1/test.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()