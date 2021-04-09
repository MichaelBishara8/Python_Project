import random as rnd

words = ["python", "media", "computation", "science"]


def main():
    word = list(rnd.choice(words))
    hidden_word = list(("_" * len(word)))
    print("Welcome to HangMan! ಠ_ಠ")
    while hidden_word != word:
        print(hidden_word)
        char = getletter()
        for i in word:
            if char in word:
                hidden_word[word.index(i)] = char

        else:
            print("Nope, try again! XXX")


def getletter():
    try:
        char = input("Enter a letter: ")
        if not char.isalpha() or len(char) != 1:
            raise TypeError("Error: A single character only")
        return char
    except TypeError:
        print("Test Error")
        getletter()


main()
