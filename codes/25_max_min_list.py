def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    return (maximum, minimum)


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Maximum and Minimum:", find_max_min(numbers))