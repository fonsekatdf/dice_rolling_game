import random

low = int(input("Enter lower bound of the range : "))
high = int(input("Enter higher bound of the range : "))

number_to_guess = random.randint(low, high)
attempts = 0
max_attempts = 5

while True:
    try:
        guess = int(input(f"Guess a the number (between {low} and {high}) : "))

        if guess < number_to_guess:
            print("Too Low!, Try again.")

        elif guess > number_to_guess:
            print("Too High!, Try again.")
        
        else:
            print(f"Congtratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

    except ValueError:
        print("Please Enter a valid number.")
    attempts += 1
   
    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
        break




    
