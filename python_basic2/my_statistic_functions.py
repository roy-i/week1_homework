def my_sum(numbers):
    # 合計値
    total = 0
    for number in numbers:
        total = total + number
    return total


def my_max(numbers):
    # 最大値
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest = number
    return biggest


def my_min(numbers):
    # 最小値
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


def my_average(numbers):
    # 平均値
    return my_sum(numbers) // len(numbers)


def main():
    text = input("データを入力してください(スペース区切り) > ")
    numbers = []
    for word in text.split():
        numbers.append(int(word))

    print(f"合計値: {my_sum(numbers)}")
    print(f"最大値: {my_max(numbers)}")
    print(f"最小値: {my_min(numbers)}")
    print(f"平均値: {my_average(numbers)}")


if __name__ == "__main__":
    main()
