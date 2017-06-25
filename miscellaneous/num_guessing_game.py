import random
print('Welcome to the number guessing game!. You have 5 chances to guess a number between 1 and 20')
count = 5

secretNumber = random.randint(1, 20)
print(secretNumber)
numberOfTries = 1
guessesLeft = 5

for i in range(5):
    if numberOfTries > 5:
        print('You reached the maximum number of tries!!')
        break
    userGuess = int(input('Please guess a whole number between 1 and 20: '))
    print(userGuess)
    if userGuess == secretNumber:
        if numberOfTries == 1:
            print('Congratulations! You guessed the correct number of {} using 1 guess!'.format(secretNumber))
        else:
            print('Congratulations! You guessed the correct number of {} using {} guesses!'.format(secretNumber, numberOfTries))
        break
    if userGuess < secretNumber:
        if numberOfTries == 5:
            print('Nope, that guess was too low and you are out of guesses. You should play again!')
            break
        else:
            print('Nope, that guess was too low - try again. You now have {} guesses left!'.format(guessesLeft - 1))
            guessesLeft -= 1
            numberOfTries += 1
            continue
    if userGuess > secretNumber:
        if numberOfTries == 5:
            print('Nope, that guess was too high and you are out of guesses. You should play again!')
            break
        else:
            print('Nope, that guess was too high - try again. You now have {} guesses left!'.format(guessesLeft - 1))
            guessesLeft -= 1
            numberOfTries += 1
            continue

