import random
print('Welcome to the number guessing game! You have '
      '5 chances to guess a number between 1 and 50')

count = 5
secretNumber = random.randint(1, 50)
print(secretNumber)

for i in range(1, count + 1):
    userGuess = int(input('Please guess a whole number between 1 and 50: '))
    if userGuess == secretNumber:
        if i == 1:
            print('Congratulations! You guessed the correct number of '
                  '{} using 1 guess!'.format(secretNumber))
        else:
            print('Congratulations! You guessed the correct number of '
                  '{} using {} guesses!'.format(secretNumber, i))
        break
    else:
        high_low = 'low' if userGuess < secretNumber else 'high'
        if i == count:  # conditional to determine when you have run out of guesses
            print('Nope, that guess was too {} and you are out of guesses. '
                  'The correct number was {}. You should play again!'
                  .format(high_low, secretNumber))
            break
        else:
            print('Nope, that guess was too {} - try again. You now '
                  'have {} guesses left!'.format(high_low, count - i))
