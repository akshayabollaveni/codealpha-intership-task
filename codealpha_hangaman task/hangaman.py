import random

words = ["cat", "dog", "book", "tree", "fish"]

word = random.choice(words)

guessed = ["_"] * len(word)
attempts = 5

print("=== HANGMAN GAME ===")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    letter = input("Enter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")

if "_" not in guessed:
    print("\n You Win!")
    print("The word is:", word)
else:
    print("\n You Lose!")
    print("The word was:", word)
