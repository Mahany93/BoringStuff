import random
number = random.randint(0,20)
print('I am thinking of a number between 1 and 20.')

while True:
    guess = int(input())
    if guess == number:
        break
    elif guess > number:
        print('Your guess is too high')
    elif guess < number:
        print('Your guess is too low')
        continue
print('Good Job! The correct number is ' + str(guess))