import random


def roll_dice(sides, times):
    results = []
    for count in range(times):
        number = random.randint(1, sides)
        results.append(number)
    return results


def main():
    sides = int(input("サイコロの面の数は?: "))
    times = int(input("何回振りますか?: "))
    results = roll_dice(sides, times)
    print(results)


if __name__ == "__main__":
    main()
