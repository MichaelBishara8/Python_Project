import random as rnd


def main():
    words = ["python", "media", "computation", "science"]
    # Randomly chooses a word
    word = list(rnd.choice(words))
    # Word is hidden, underscores are a clue to how many letters
    hidden_word = list(("_" * len(word)))

    print("Welcome to HangMan! ಠ_ಠ")

    # Loop will continue till solved
    while hidden_word != word:
        print_list(hidden_word)
        char = get_letter()
        # check for repeated letters
        if char in hidden_word:
            print(char, "has already been entered!")
            continue
        # Updates hidden_word with correct char for all occurrences
        elif char in word:
            for i, hidden_letter in enumerate(word):
                if hidden_letter == char:
                    hidden_word[i] = char
        else:
            print("Nope, try again!")
    print("Congrats! The word was:", ''.join(word).capitalize() + '!')


# Tests the letter is alpha, a single character and makes it lowercase,
# otherwise it asks to re-enter

# Requests input and tests that it is alphabetical and singular then returns a lowercase char
def get_letter():
    try:
        char = input("Enter a letter: ")
        if not char.isalpha() or len(char) != 1:
            raise TypeError("Error: Incorrect input")
        return char.lower()
    except TypeError:
        print("Error: Only a single character - no numbers/symbols")
        get_letter()


# Prints the list as a string
def print_list(word_list):
    print(''.join(word_list))


if __name__ == "__main__":
    main()

# get_letter() should be smaller [Coupling and cohesion]

# todo Solve all at once
# todo other exceptions to catch
