import random

#converts the random int into heads or tail strings
def setToss(num):
    if num == 1:
        return 'heads'
    else:
        return 'tails'    
    

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads #first issue, toss is a number, not string
assert toss == 0 or 1  #not needed since random.randint seemed to work.
if setToss(toss) == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if setToss(toss) == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
