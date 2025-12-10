import random

# 5 predefined words
words = ["apple", "banana", "chocolate", "python", "friend"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman!")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", used_letters)

    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already used this letter! Try again.")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong!")
        attempts -= 1

    if "_" not in guessed:
        print("\n🎉 YOU WON! The word was:", word)
        break

if "_" in guessed:
    print("\n❌ YOU LOST! The word was:", word)
m
