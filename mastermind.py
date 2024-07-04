import random


def round_game(number_of_round):
    print(f"Round {number_of_round}")


def check_code(code):
    if len(code) != 4 or '0' in code:
        return False
    try:
        int(code)
        unique_digits = set(code)
        if len(unique_digits) == 4:
            return True
        else:
            return False
    except ValueError:
        return False


def count_correct_and_misplaced(secret_code, guess):
    correct = 0
    misplaced = 0
    for i in range(len(secret_code)):
        if secret_code[i] == guess[i]:
            correct += 1
        elif guess[i] in secret_code:
            misplaced += 1
    return correct, misplaced


def play_game():
    secret_code = str(random.randint(1000, 9999))
    print("Will you find the secret code?")
    print("Please enter a valid guess")
    round_number = 0
    while round_number < 10:
        round_game(round_number)
        code = input("> ")
        if not check_code(code):
            print("Invalid input. Please enter a 4-digit code without 0.")
            continue
        correct, misplaced = count_correct_and_misplaced(secret_code, code)
        print(f"Well placed pieces: {correct}\nMisplaced pieces: {misplaced}")
        round_number += 1
        if code == secret_code:
            print(f"Congratulations! You found the secret code in {round_number} rounds.")
            break
    else:
        print(f"Sorry, you couldn't find the secret code. The code was {secret_code}.")


def help_game():
    print("Mastermind is a game composed of 9 pieces of different colors. A secret code is then composed of 4 "
          "distinct pieces.")
    print("The player has 10 attempts to find the secret code. After each input, the game indicates to the player the "
          "number of well placed pieces and the number of misplaced pieces.")
    print("Pieces will be '1' '2' '3' '4' '5' '6' '7' '8' '9'.")
    print("If the player finds the code, he wins, and the game stops. A misplaced piece is a piece that is present in "
          "the secret code but that is not in a good position.")
    print("You must read the player's input from the standard input.")
    print("Your program will also receive the following parameters: -c [CODE]: specifies the secret code."
          " If no code is specified, a random code will be generated. -t [ATTEMPTS]: specifies the number of attempts;"
          " by default, the players 10 attempts.")
    s = input("You want to play a game? (yes/no): ").lower()
    if s == 'yes':
        return play_game()
    else:
        return


def main_game():
    print("h - how to play")
    print("p - Start game")
    while True:
        answer = input("Choose answer: ").lower()
        if answer == 'h' or answer == 'p':
            if answer == 'h':
                help_game()
            else:
                play_game()
            break
        else:
            continue


main_game()
