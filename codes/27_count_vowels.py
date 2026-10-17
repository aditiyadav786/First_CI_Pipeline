def count_vowels(text):
    count = 0

    for character in text.lower():
        if character in "aeiou":
            count += 1

    return count


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Number of vowels:", count_vowels(text))