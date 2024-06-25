import random

retry_num = 0

while True:
    secret_number = random.randint(1,10)
    guess = int(input('I\'m thinking of a number between 1 - 10. Can you guess the number? '))
    match guess: 
        case n if guess == secret_number:
            print('Congratulations, you guessed it!')
        case n if guess > secret_number:
            print('Oops, your guess is a bit high. Try again!')
        case n if guess < secret_number:
            print('Nope, your guess is a bit low. Give it another shot!')
        case _:
            print('invalid')
    replay = input('Would you like to play again? (yes/no) ').lower()
    if replay == 'yes':
        retry_num += 1
    else:
        print('Thanks for playing!')
        break
print(f'You replayed {retry_num} times.')
