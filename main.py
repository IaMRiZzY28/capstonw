import random
luca=1
cula=10
lacu=2
secret_number=random.randint(luca,cula)


def get_guess():
    while True:
        guess= int(input("guess number between 1 to 10:"))
        if luca <= guess <= cula:
            return guess
        else:
            print("invalid input. please enter number within 1 to 10")


def check_guess(guess,secret_number):
    if guess == secret_number:
        return "coorect"
    elif guess < secret_number:
        return "too low"
    else:
        return "too high"
    

def play_game():
    attempts = 0
    won = False


    while attempts < lacu:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess,secret_number)
        if result == "coorect":
            print(f"congratulations")
            won=True
            break
        else:
            print(f"try again")
    if not won:
        print(f"you ran out of attempts")


if __name__=="__main__":
    print("welcome")
    play_game()