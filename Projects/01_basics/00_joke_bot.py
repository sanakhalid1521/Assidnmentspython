import random

def joke_bot():
    jokes = [
        "Teacher: Tumhari kitaab kahan hai? \nStudent: Sir, wo toh history ban chuki hai! 😆",
        "Biwi: Tum mujhe kitna pyar karte ho? \nShohar: Jitna tum makeup karti ho! 😂",
        "Pathan: Doctor sahab, jab aankh band karta hoon to andhera ho jata hai! 😜",
        "Teacher: 2 aur 2 kitne hote hain? \nStudent: Sir, 4. \nTeacher: Aqalmand bano! \nStudent: Sir, 22! 🤣",
        "Ladka: Mujhe tere pyar mai pagalpan ho gaya hai! \nLadki: Toh doctor ke paas jao! \nLadka: Doctor tu mai tere liye hi bana tha! 😍😂"
    ]
    print(random.choice(jokes))

if __name__ == "__main__":
    joke_bot()
