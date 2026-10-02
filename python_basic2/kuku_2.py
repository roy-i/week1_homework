def create_kuku_table(rows, columns):
    table = []
    for row in range(1, rows + 1):
        line = []
        for column in range(1, columns + 1):
            number = row * column
            line.append(number)
        table.append(line)
    return table


def main():
    rows = int(input("行数を入力してください: "))
    columns = int(input("列数を入力してください: "))
    table = create_kuku_table(rows, columns)

    for line in table:
        for number in line:
            print(f"{number} ", end="")
        print()


if __name__ == "__main__":
    main()
