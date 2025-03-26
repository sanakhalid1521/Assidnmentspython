import random

def guess_my_number():
    secret_number = random.randint(1, 100)
    guess = 0
    
    while guess != secret_number:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("🎉 Congratulations! You guessed the right number.")

if __name__ == "__main__":
    guess_my_number()
