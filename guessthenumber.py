import random

def play():
    min_for_range = 1
    max_for_range = 10
    chances = 5

    while True:
        secret_number = random.randint(min_for_range, max_for_range)
        print(f'\nI have chosen a number between {min_for_range} and {max_for_range}.\nYou have {chances} chances to guess the number.')
        
        attempt = 0  
        while attempt < chances:
            guess = input(f'Attempt {attempt + 1}/{chances}. Enter your guess:\t')

            if not guess.isnumeric():
                print("Please enter a valid number.")
                continue  
            
            guess = int(guess)
            attempt += 1 

            if secret_number == guess:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")  
                play_again = input('\nDo you want to play again with a wider range? (yes/no): ').strip().lower()
                if play_again == 'no':
                    print('Good Bye.')
                    return
                elif play_again != 'yes':
                    print("Please enter yes or no.")
                max_for_range += 5
                chances += min_for_range
                break
            elif secret_number > guess:
                print("Hint: The number is above your guess.")
            else:
                print("Hint: The number is below your guess.")
        else:
            print(f"Sorry, you're out of chances! The correct number was {secret_number}.")
            hi = input('\nDo you want to play again? (yes/no): ').strip().lower()
            if hi != 'yes':
                print('Good Bye.')
                return

play()