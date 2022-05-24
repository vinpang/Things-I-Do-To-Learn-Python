import random
from math import ceil, log

print('What is your name?')
name = input()

print('Hi ',name,'. We\'re going to play a guessing game today. I\'m going to think of a number between 1 and a number and you\'re going to give me. You\'re then going to guess my number. If you guess wrong I\'ll tell you whether you need to go higher or lower')
print(' Please select the upper number?')
b = 0
while b < 2:
    try:
        print('Please enter a number greater than 1')
        b = int(input())
    except ValueError:
        pass

print('Select difficulty. How many guesses do you want?')
num_guesses = 0
while num_guesses < 2:
    try:
        print('Please enter a number greater than 1')
        num_guesses = int(input())
    except ValueError:
        pass

secretnumber = random.randint(1,b) 
# edit here to insert a fixed value
print('OK ',name,'. I am thinking of a number between 1 and ',b,'. You have ',num_guesses,' guesses. ',end='')

optimalguesses = ceil(log(b)/log(2))
nearestroot = optimalguesses 

if num_guesses < optimalguesses:
    print('You\'re gonna have to get lucky')
else:
    print('You can do it!')

# Ask the player to guess X times
for guessesTaken in range (1,num_guesses+1): #+ 1 #to account for upper range being the < rather than <=
    print('Take a guess. You have',num_guesses - guessesTaken + 1,' left')
    guess = int(input())
    if guess < secretnumber:
        print('Higher')
    elif guess > secretnumber:
        print('Lower')
    else:
        break

if guess == secretnumber:
    print('Correct',name,'! You guessed in',guessesTaken,' goes.')
    failed = False
else:
    print('Nope. The number I was thinking of was',str(secretnumber),'. Better luck next time.')
    failed = True

print('Guaranteed solution in '+str(optimalguesses))
# value that is 2**n, should be able to guess within n goes

if num_guesses >= optimalguesses and guessesTaken >= optimalguesses:
    print('Did you know you could have done better. Show aut solution? (Y/N)')
    choice = input()
    if choice == 'N':
        print('END')
    else:
        currentAIguess = ceil(b/2)
        for iteration in range(0,num_guesses):
            print('AI Guess ' + str(iteration+1) + ': ' + str(currentAIguess))
            if currentAIguess < secretnumber:
                print('Higher')
                currentAIguess += 2**(nearestroot - iteration - 1 - 1)
            elif currentAIguess > secretnumber:
                print('Lower')
                currentAIguess -= 2**(nearestroot - iteration - 1 - 1)
            else:
                print('AI solution found in '+str(iteration+1)+' goes. This is why the robots will always win.')
                break

# aim - develop a bot that can beat this game 100% of the time where b = 2**n and num_guesses = n+1