def format_kuku(rows, columns):
    lines = []
    for row in range(1, rows + 1):
        line = ""
        for column in range(1, columns + 1):
            number = column * row
            if number < 10:
                line = line + f"{column} x {row} =  {number} | "
            else:
                line = line + f"{column} x {row} = {number} | "
        lines.append(line)
    return lines


def main():
    rows = int(input("行数を入力してください: "))
    columns = int(input("列数を入力してください: "))
    lines = format_kuku(rows, columns)

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
