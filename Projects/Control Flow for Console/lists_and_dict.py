def main():
    """List operations with user interaction."""
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("\n🍉 **Welcome to List Practice!** 🍊")
    print(f"🔹 Initial fruit list: {fruit_lst}")

    while True:
        print("\nChoose an operation: **add**, **remove**, **display**, **sort**, **exit**")
        choice = input("🔹 Enter your choice: ").strip().lower()

        if choice == "add":
            fruit = input("Enter the fruit to add: ").strip().lower()
            fruit_lst.append(fruit)
            print(f"✅ Updated list: {fruit_lst}")

        elif choice == "remove":
            fruit = input("Enter the fruit to remove: ").strip().lower()
            if fruit in fruit_lst:
                fruit_lst.remove(fruit)
                print(f"✅ {fruit} removed! Updated list: {fruit_lst}")
            else:
                print("❌ Error: Fruit not found in the list.")

        elif choice == "display":
            print(f"📜 Fruit List ({len(fruit_lst)} items): {', '.join(fruit_lst)}")

        elif choice == "sort":
            fruit_lst.sort()
            print(f"✅ Sorted list: {fruit_lst}")

        elif choice == "exit":
            print("👋 Exiting List Practice. Have a great day!")
            break

        else:
            print("❌ Invalid choice! Please select **add, remove, display, sort, or exit**.")

if __name__ == "__main__":
    main()
