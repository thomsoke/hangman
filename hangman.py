###########################################################
# re-write of previous python hangman project
# original: 11-26-2018
# re-write: 12-23-2019
###########################################################

###########################################################
def get_secret_phrase(secret_phrase):
    secret_phrase = input("enter word or phrase: ")
    return secret_phrase


###########################################################
def get_user_guess(user_guess):
    user_guess = input("enter a letter to guess: ")
    return user_guess


###########################################################
def compare_user_guess(secret_phrase, current_phrase, user_guess):
    correct_guess = 0
    strike_guess = 0
    correct = False

    for i in range(len(secret_phrase)):
        if(secret_phrase[i]) == user_guess:
            correct_guess += 1
            current_phrase[i] = user_guess
            print("correct guess")
            correct = True
        else:
            strike_guess += 1
            print("strike")
            correct = False
    return current_phrase, correct_guess, strike_guess, correct


###########################################################
def check_win(current_phrase, strike_guess, win):
    counter = 0
    win = False

    if(strike_guess < 6):
        for i in range(len(current_phrase)):
            if((current_phrase[i]) == "_"):
                counter += 1
                if (counter > 0):
                    win = False
                else:
                    win = True
    else:
        win = False

    return win


###########################################################
def print_hangman(strike_guess):
    if strike_guess == 0:
        print("   __")
        print("  |  |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("-------")

    elif strike_guess == 1:
        print("   __")
        print("  |  |")
        print("  0  |")
        print("     |")
        print("     |")
        print("     |")
        print("-------")

    elif strike_guess == 2:
        print("   __")
        print("  |  |")
        print("  0  |")
        print("  |  |")
        print("     |")
        print("     |")
        print("-------")

    elif strike_guess == 3:
        print("   __")
        print("  |  |")
        print("  0  |")
        print(" \|  |")
        print("     |")
        print("     |")
        print("-------")

    elif strike_guess == 4:
        print("   __")
        print("  |  |")
        print("  0  |")
        print(" \|/ |")
        print("     |")
        print("     |")
        print("-------")

    elif strike_guess == 5:
        print("   __")
        print("  |  |")
        print("  0  |")
        print(" \|/ |")
        print(" /   |")
        print("     |")
        print("-------")

    elif strike_guess >= 6:
        print("   __")
        print("  |  |")
        print("  0  |")
        print(" \|/ |")
        print(" / \ |")
        print("     |")
        print("-------")
        print("u ded")

    else:
        print("   __")
        print("  |  |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("-------")



###########################################################
###########################################################
def main():

    secret_phrase = ""
    user_guess = ""
    win = False

    get_secret_phrase(secret_phrase)
    current_phrase = ['_'] * len(secret_phrase)

    while (win == False):
        get_user_guess(user_guess)
        compare_user_guess(secret_phrase, current_phrase, user_guess)
        current_phrase, correct_guess, strike_guess = compare_user_guess(secret_phrase, current_phrase, user_guess)

        print(current_phrase)
        print(correct_guess)
        print(strike_guess)
        print(correct_bool)

        print(print_hangman(strike_guess))

        check_win(current_phrase, strike_guess, win)


main()
