import re
import resource
import time

import csv

import random

import winsound


name = input("What is your name? :")

print("Hi,"+name, "Time to play hangman game")

print()

time.sleep(1)

print("Start Loading...")

time.sleep(0.5)

words = []

with open('./resource/word_list.csv','r') as f:
    reader = csv.reader(f)
    next(reader)

    for c in reader:
        words.append(c)

random.shuffle(words)

q = random.choice(words)



word = q[0].strip()
guessus = ''

turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guessus:
            print(char, end =' ')
        else:
            print("_", end = ' ')
            failed += 1
    if failed == 0:
        print()
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Congratulations!')
        break
    print()

    print('Hint : {}'.format(q[1].strip()))
    guess =input('guess a character :')

    guessus += guess

    if guess not in word:
        turns -= 1

        print("Oops!")
        print("You have", turns, "more guesses")

        if turns == 0:
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            print("bye,",name)

