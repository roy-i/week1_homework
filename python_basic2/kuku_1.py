def create_kuku_table():
    table = []
    for rows in range(1, 10):
        line = []
        for columns in range(1, 10):
            number = rows * columns
            line.append(number)
        table.append(line)
    return table


def main():
    table = create_kuku_table()

    for line in table:
        for number in line:
            print(f"{number} ", end="")
        print()


if __name__ == "__main__":
    main()
