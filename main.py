import random as rnd

words = ["python", "media", "computation", "science"]


def main():
    word = list(rnd.choice(words))
    hidden_word = ("_" * len(word))
    print("Welcome to HangMan! ಠ_ಠ")
    while hidden_word != word:
        print(hidden_word)
        char = getletter()
        if char in word:
            for i in word:
                hidden_word[i] = char


def getletter():
    try:
        char = input("Enter a letter: ")
        if char is not type(char):
            raise TypeError("Error: A single character only")
        return char
    except TypeError:
        print("Test Error")
        getletter()

main()