import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter = random.choice(alphabet)
guess_count = 0
correct = alphabet.index(letter) + 1
while guess_count < 3:
    guess = input("Guess what letter of the alphabet " + letter + " is:")
    if guess == str(correct):
        print("You got it right!")
        break
    elif guess != str(correct):
        guess_count = guess_count + 1
        if guess_count == 3:
            break
print("Hope you enjoyed the game!")



