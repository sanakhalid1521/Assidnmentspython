import time

def liftoff():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)  # 1 second delay for real countdown effect
    print("🚀 Liftoff!")

if __name__ == "__main__":
    liftoff()
