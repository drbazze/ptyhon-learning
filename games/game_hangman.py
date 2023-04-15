"""
Project: Game hanger
"""

import random
import os

DEBUG = True

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = [
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]
user_life = 6
end_of_the_game = False

random_word = random.choice(word_list)
random_word_length = len(random_word)
display = []

for _ in range(random_word_length):
    display += "_"

if DEBUG:
    print(random_word)

print(logo)

while not end_of_the_game:
    guessed_letter = input("Guess a letter: ").lower()

    os.system('cls' if os.name == 'nt' else 'clear')

    for index in range(random_word_length):
        letter = random_word[index]

        if letter == guessed_letter:
            display[index] = letter
    
    #Print the results on the screen
    print(stages[user_life])
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    #Check if the letter is in the word string
    if guessed_letter not in random_word:
        user_life -= 1
        print(f"The letter is not presented in the word. Lost one life, {user_life} is remaining\n")

    #Check if the game is ended or not
    if display.count("_") == 0 or user_life  == 0:
        end_of_the_game = True

if user_life > 0:
    print("You won!")
else:
    print(f"You lost, the word was: {random_word}")