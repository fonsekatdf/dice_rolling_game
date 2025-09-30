import random

num_dice = int(input("How many dice do you want to roll? : "))
all_rolls = []
count = 0

while True:
    choice = input("Roll the dice? (y/n) : ").lower()
    if choice == "y":
        roll = [random.randint(1, 6) for _ in range(num_dice)]
        all_rolls.append(roll)
        print(f"({', '.join(map(str, roll))})")
        count += 1

    elif choice == "n":
        print(f"You rolled dice {count} times.")
        print("Thank you for playing!")
        break
    
    else:
        print("Invalid choice!")



     

