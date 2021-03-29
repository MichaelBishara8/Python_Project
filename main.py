import random as rnd

words = ["python", "media", "computation", "science"]

def main():
    word = rnd.choice(words)
    print("Welcome to HangMan! ಠ_ಠ")
    print("_" * len(word))


if __name__ == "__main__":
    main()
