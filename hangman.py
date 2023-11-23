import time


def introduce_players():
    player1 = input("Hi Player 1, Please enter your name? ")
    print(f"Hi, {player1}, Welcome to Hangman!")

    time.sleep(1)

    player2 = input("Hi player 2, please enter your name? ")
    print(f"Hi, {player2}, Try your best to trick your opponent!")

    time.sleep(2)

    return player1, player2


def get_secret_word():
    word = input("Please enter the word you want to be guessed: ")
    turns = int(input("Enter the number of chances your opponent will have (8 is the maximum!): "))
    return word, turns


def print_current_state(word, guesses):
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("__", end=' ')
    print()


def play_hangman(word, turns):
    guesses = " "

    while turns > 0:
        count = 0
        print_current_state(word, guesses)

        for char in word:
            if char not in guesses:
                count += 1

        if count == 0:
            print("\nYou won! The hangman was saved.")
            break

        guess = input("\nGuess a character: ").lower()
        guesses += guess

        if guess not in word:
            turns -= 1
            print(f"\nWrong! '{guess}' is not in the word.")
            print(f"You have {turns} turns left. Keep guessing!\n")
            draw_hangman(turns)

        if turns == 0:
            print("\nUnfortunately, you did not find the secret word. Better luck next time!")
            draw_hangman(turns)
            break


def draw_hangman(turns):
    hangman_stages = [
        ["   ________      ", "   |      |     ", "   |      |     ", "   |             ", "   |             "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |             "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     ",
         "   |      |     "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     ",
         "   |     /|\    "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     ",
         "   |     /|\    "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     ",
         "   |     /|\    "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     ",
         "   |     /|\    "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     ",
         "   |     /|\    "],
        ["   ________      ", "   |      |     ", "   |      |     ", "   |      o     ", "   |      |     ",
         "   |     /|\    ", "   |     / \    "]
    ]

    for stage in hangman_stages[8 - turns:]:
        print("\n".join(stage))


def main():
    player1, player2 = introduce_players()
    word, turns = get_secret_word()

    print(f"\nTime to start guessing, {player1}! You have {turns} chances to guess the secret word.")
    print('\n' * 40)
    time.sleep(2)

    play_hangman(word, turns)


if __name__ == "__main__":
    main()
