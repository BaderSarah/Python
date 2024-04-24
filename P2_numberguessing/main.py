import random


def play_guess_number():
    guessed = False
    number = random.randint(0, 20)
    print("Let's play \"guess the number\" (0-20)!")
    while guessed is False:
        users_guess = give_users_guess()
        if users_guess > number:
            print("too high")
        elif users_guess < number:
            print("too low")
        else:
            print("correct!")
            guessed = True


def give_users_guess():
    while True:
        users_guess = input("guess: ")
        if users_guess.isdigit():
            return int(users_guess)
        else:
            print("You didn't enter a number, try again...")


def main():
    play_guess_number()


if __name__ == "__main__":
    main()