#!/usr/bin/env python3

import random

def guess():
    number =  random.randint(1,10)
    attempts = 3
    while attempts > 0:
        guess = input('guess a number between 1 and 10: ')
        if int(guess) == int(number):
            print('You guessed it!')
            break
        elif int(guess) != int(number):
            print(f'Try again you have {attempts - 1} attempts left')
            attempts -= 1
        if attempts == 0:
            print(f'Sorry try again the number was {number}')
    return int(guess)
               
guess()