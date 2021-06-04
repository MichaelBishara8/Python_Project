import random as rnd


def main():
    words = ["python", "media", "computation", "science"]
    score = 0
    allowed_attempts = 5
    # Randomly chooses a word
    word = list(rnd.choice(words))
    # Word is hidden, underscores are a clue to how many letters
    hidden_word = list(("_" * len(word)))

    print("Welcome to HangMan! ಠ_ಠ")

    # Loop will continue till solved or 5 incorrect attempts
    while hidden_word != word and allowed_attempts > 0:
        print(''.join(hidden_word))
        char = get_letter()
        # check for repeated letters
        if char in hidden_word:
            print(char, "has already been entered!")
            score -= 1
            continue
        # Updates hidden_word with correct char for all occurrences
        elif char in word:
            for i, hidden_letter in enumerate(word):
                if hidden_letter == char:
                    hidden_word[i] = char
                    score += 3
        else:
            print("Nope, try again!\nYou have", allowed_attempts, "attempts remaining!")
            score -= 1
            allowed_attempts -= 1
    if allowed_attempts > 1:
        print("Congrats! The word was:", ''.join(word).capitalize() + '!')
        print("You scored:", score)
    else:
        score -= 5
        print("Bad luck! The word was:", ''.join(word).capitalize() + '!')
        print("You scored:", score)


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


if __name__ == "__main__":
    main()

# get_letter() should be smaller [Coupling and cohesion]

# todo Solve all at once
# todo other exceptions to catch
