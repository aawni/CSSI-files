from random import randint
my_num= randint(1,10);

while (True):
    userGuess = input('Guess a number between 1-10')
    if userGuess==my_num:
        print "you win!"
    elif userGuess>my_num and userGuess<=10:
        print "your guess is too high"
    elif userGuess<my_num and userGuess>=1:
        print "your guess is too low"
    else:
        print "please enter a number between 1 and 10"
