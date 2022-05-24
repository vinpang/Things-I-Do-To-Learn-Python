import random
import math

print('Hello. What is your name?')
name = input()

print('Select difficulty. Upper range?')
b = 0
while b < 2:
    try:
        print('Please enter a number greater than 1')
        b = int(input())
    except ValueError:
        pass

print('Select difficulty. Number of guesses?')
num_guesses = 0
while num_guesses < 2:
    try:
        print('Please enter a number greater than 1')
        num_guesses = int(input())
    except ValueError:
        pass

secretnumber = random.randint(1,b)
print('OK ',name,'. I am thinking of a number between 1 and ',b,'. You have ',num_guesses,' guesses.')

# Ask the player to guess X times
for guessesTaken in range (1,num_guesses+1): #+ 1 #to account for upper range being the < rather than <=
    print('Take a guess')
    guess = int(input())
    if guess < secretnumber:
        print('Higher')
    elif guess > secretnumber:
        print('Lower')
    else:
        break

if guess == secretnumber:
    print('Correct',name,'! You guessed in',guessesTaken,'.')
else:
    print('Nope. The number I was thinking of was',str(secretnumber),'. Better luck next time.')

# aim - develop a bot that can beat this game 100% of the time where b = 2**n and num_guesses = n+1