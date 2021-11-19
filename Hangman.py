#  "Hangman" project by Zsolt Pal
#  2021
import random
import string

def title():
    hangman_logo = ["H", "A", "N", "G", "M", "A", "N"]
    banner = " ".join(hangman_logo)
    print(f"{banner}")


def word_supplier():
    # the library and returning one random word from library
    library = ['python', 'java', 'kotlin', 'javascript']  # comment out and use the ones below to test
    picked_word = random.choice(library)
    return [char for char in picked_word]


def get_input():
    # simple getter method
    return input(f'Input a letter: ')


def menu():
    while True:
        user_input = input('Type "play" to play the game, "exit" to quit:')
        if user_input == "play":
            return True
        if user_input == "exit":
            return False


def hangman():
    tries = 8  # number of "lives"
    entered_letters = []  # keeping track of entered letters
    title()
    while menu():
        word_to_guess = word_supplier()
        hidden_word = ["-" for _ in word_to_guess]
        while tries > 0:
            print("")
            print("".join(hidden_word))
            user_letter = get_input()
            entered_letters.append(user_letter)  # keeping track of entered letters
            # logic block
            if len(user_letter) != 1:
                print("You should input a single letter")
            elif user_letter not in string.ascii_lowercase:
                print("Please enter a lowercase English letter")
            elif entered_letters.count(user_letter) > 1:  # checking if the input appears more than once in the list
                print("You've already guessed this letter")
            elif user_letter in word_to_guess:
                for index in range(len(word_to_guess)):
                    if word_to_guess[index] == user_letter:
                        hidden_word[index] = user_letter
            else:
                print("That letter doesn't appear in the word")
                tries -= 1
            if "-" not in hidden_word:
                print("")
                print("".join(hidden_word))
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You lost!")
            print("")
    else:
        print("Thank you for playing! Have a nice day.")

hangman()