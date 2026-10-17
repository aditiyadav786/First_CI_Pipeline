def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    if len(first) != len(second):
        return False

    first_count = {}
    second_count = {}

    for char in first:
        first_count[char] = first_count.get(char, 0) + 1

    for char in second:
        second_count[char] = second_count.get(char, 0) + 1

    return first_count == second_count


if __name__ == "__main__":
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    print(is_anagram(first, second))