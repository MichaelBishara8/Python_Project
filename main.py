import random as rnd

words = ["python", "media", "computation", "science"]


def main():
    word = list(rnd.choice(words))
    hidden_word = list(("_" * len(word)))

    print("Welcome to HangMan! ಠ_ಠ")

    while hidden_word != word:
        print_list(hidden_word)
        char = get_letter()
        if char in word:
            for i, hidden_letter in enumerate(word):
                if hidden_letter == char:
                    hidden_word[i] = char
        else:
            print("Nope, try again! XXXabc")
    print("Congrats!")


def get_letter():
    try:
        char = input("Enter a letter: ")
        if not char.isalpha() or len(char) != 1:
            raise TypeError("Error: Incorrect input")
        return char
    except TypeError:
        print("Error: Only a single character - no numbers/symbols")
        get_letter()


def print_list(word_list):
    print(''.join(word_list))


main()


# todo Check repeated letters
# todo Scoreboard/players?
# todo other exceptions to catch
