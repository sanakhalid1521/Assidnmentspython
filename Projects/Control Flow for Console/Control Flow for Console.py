import random

NUM_ROUNDS = 5

def get_random_encouragement():
    messages = [
        "Great job! Keep it up! 🎉",
        "You're on fire! 🔥",
        "That was awesome! 🚀",
        "Keep going! You're doing great! 💪",
        "Whoa! You're a natural at this! 🌟"
    ]
    return random.choice(messages)

def get_random_loss_message():
    messages = [
        "Oops! Better luck next time! 😅",
        "Ah, so close! Try again! 🎯",
        "A tough one! But don't give up! 💡",
        "No worries! You'll get it next time! 🌈",
        "Well played! The game is still on! 🏆"
    ]
    return random.choice(messages)

def main():
    print("🎲 Welcome to the High-Low Game! 🎲")
    print('-' * 40)

    score = 0  

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"\n🔥 Round {round_num} 🔥")
        
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        
        print(f"Your number is: {your_num}")
        
        # Get valid user input
        choice = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        
        while choice not in ["higher", "lower"]:
            choice = input("❗ Invalid choice! Please enter 'higher' or 'lower': ").strip().lower()

        # Check if the player guessed correctly
        if (choice == "higher" and your_num > computer_num) or (choice == "lower" and your_num < computer_num):
            print(f"✅ Correct! The computer's number was {computer_num}. {get_random_encouragement()}")
            score += 1
        else:
            print(f"❌ Oops! The computer's number was {computer_num}. {get_random_loss_message()}")

        print(f"📊 Your score is now: {score}")
        print('-' * 40)

    # Game Over Summary
    print("\n🎮 Game Over! 🎮")
    print(f"🏁 Your final score: {score}/{NUM_ROUNDS}")

    if score == NUM_ROUNDS:
        print("🎖️ Wow! You played perfectly! You're a champion! 🏆")
    elif score >= NUM_ROUNDS // 2:
        print("👏 Great game! You did really well! Keep it up! 🚀")
    else:
        print("😅 Better luck next time! Keep practicing! 🎯")

if __name__ == "__main__":
    main()
