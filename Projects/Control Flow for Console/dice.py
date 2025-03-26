def access_element(lst, index):
    """Access an element from the list safely."""
    try:
        return f"✅ Element at index {index}: {lst[index]}"
    except IndexError:
        return "❌ Error: Index out of range."

def modify_element(lst, index, new_value):
    """Modify an element at a given index in the list."""
    try:
        lst[index] = new_value
        return f"✅ List updated: {lst}"
    except IndexError:
        return "❌ Error: Index out of range."

def slice_list(lst, start, end):
    """Return a slice of the list."""
    try:
        return f"✅ Sliced list: {lst[start:end]}"
    except IndexError:
        return "❌ Error: Invalid indices."

def index_game():
    """Main game loop for list operations."""
    lst = [1, 2, 3, 4, 5]
    print("\n🎮 **Welcome to the Index Game!** 🎮")
    
    while True:
        print("\nCurrent List:", lst)
        print("Choose an operation: **access**, **modify**, **slice**, or **exit**")
        operation = input("🔹 Enter operation: ").strip().lower()

        if operation == "access":
            try:
                index = int(input("Enter index to access: "))
                print(access_element(lst, index))
            except ValueError:
                print("❌ Error: Please enter a valid integer.")
        
        elif operation == "modify":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(lst, index, new_value))
            except ValueError:
                print("❌ Error: Please enter a valid integer.")
        
        elif operation == "slice":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(slice_list(lst, start, end))
            except ValueError:
                print("❌ Error: Please enter valid integers.")
        
        elif operation == "exit":
            print("👋 Exiting the game. Thanks for playing!")
            break
        
        else:
            print("❌ Invalid operation. Please choose **access, modify, slice, or exit**.")

if __name__ == "__main__":
    index_game()
