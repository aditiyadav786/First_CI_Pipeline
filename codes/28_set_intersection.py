def set_intersection(first, second):
    common = set()

    for item in first:
        if item in second:
            common.add(item)

    return common


if __name__ == "__main__":
    first = set(map(int, input("Enter first set elements: ").split()))
    second = set(map(int, input("Enter second set elements: ").split()))
    print("Intersection:", set_intersection(first, second))