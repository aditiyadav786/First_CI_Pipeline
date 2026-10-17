import string


def largest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        cleaned_word = word.strip(string.punctuation)

        if len(cleaned_word) > len(longest):
            longest = cleaned_word

    return longest


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Largest word:", largest_word(sentence))