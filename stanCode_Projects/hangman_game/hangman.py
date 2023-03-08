"""
File: hangman.py
Name: Audrey Tsang
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will generate a random word and gives user a dashed word,
    user can input one character each round, if the user input is correct,
    the program will show the updated word on console.
    """
    guess()


def guess():
    """
    This function asks user input an alphabet, and checks if it is correct.
    If the alphabet is correct, the function will un-dashed the part,
    otherwise user will lose one chance to guess.
    """
    word = random_word()    # Generate a random word
    print("The word looks like ", end='')
    ans = ""
    for i in range(len(word)):
        ans += '-'
    print(ans)
    n = N_TURNS
    while True:
        if n > 0:
            print("You have " + str(n) + " wrong guesses left.")
            input_ch = input('Your guess: ')
            ch = check(input_ch)
            new_ans = ""
            if ch in word:
                print('You are correct!')
                position = word.find(ch)
                for i in range(len(word)):
                    if i == position:
                        new_ans += ch
                        others = word[position + 1:]  # Check if there's other correct alphabet
                        if ch in others:
                            position = position+others.find(ch)+1
                    else:
                        new_ans += ans[i]
                if new_ans.isalpha():   # Check if user guess out all alphabets
                    print("You win!")
                    break
                else:
                    print("The word looks like " + new_ans)
                    ans = new_ans   # Renew the record of user guesses
            else:
                print("There is no " + ch + "'s in the word.")
                n -= 1
        else:
            print("You are completely hung : (")
            break
    print("The word was: " + word)


def check(a):
    """
    This function checks if the input is an alphabet and capitalize it.
    """
    while not a.isalpha() or len(a) > 1:  # Check if the input is an alphabet
        print("illegal format.")
        a = input('Your guess: ')
    if a.islower():     # If the alphabet is lower case, capitalize it
        a = a.upper()
    return a


def random_word():
    """
    This function generate random words.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
