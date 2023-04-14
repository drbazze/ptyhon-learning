"""
Project description:
- The project scope is to generate a random number and ask the player to guess it. The game ends if the player hit the random number.

Requirements:
- The random number must be in a range of 1-100. 
- The player has unlimited guesses. 
- If the player enters a number the app must tell if it's higher or lower to the random number.
- After every 5 tries the app will send a motivation message to the player in order to keep the motivation

Error handling:
- If the input is NaN, then an error must appear and ask for another number

Author:
- Tamas Zumpf
- Version: 1.0
"""

#Includes
import random
from colorama import Back, Fore, Style

#Debug flag
DEBUG = False

def play():
    #The target number
    secret_number = random.randint(1, 100)
    #The player's guess number
    guess_number = 0
    #Number of max tries in hard difficulty it's 5
    max_tries = 10
    #Number of tries
    tries = 0
    #Threshold for showing the motivation messages
    show_message_after_tries = 3

    #Declaration of the motivation messages
    messages = ["Keep up the good work!"
                ,"You're almost there!"
                ,"Every guess gets you closer to the correct answer!"
                ,"Stay focused and keep guessing, you've got this!"
                ,"Believe in yourself and trust your instincts."
                ,"You've come this far, don't let a few wrong guesses stop you."]

    #Welcome message
    print(f"{Fore.BLUE}Welcome to the guess number game.\n{Fore.LIGHTYELLOW_EX}The rule is simple, I was thinking a number between 1 and 100, your task is to quess it.\n{Fore.LIGHTRED_EX}Show me your talent!")
    print(Style.RESET_ALL)

    #Show the magic number in debug mode
    if DEBUG:
        print(f"[secretNumber: {secret_number}]")

    if (input("Choose a difficulty. Type 'easy' or 'hard': ") == "hard"):
        max_tries = 5

    print(f"Max trias: {max_tries}")

    #The main program execution
    while guess_number != secret_number and tries < max_tries:
        #Get the input form the player
        guessInput = input(f"{Fore.CYAN}--Guess a number: ")
        print(Style.RESET_ALL)
        #Increase the tries counter
        tries += 1
        
        #Error handling, if the input is not an integer
        try:
            guess_number = int(guessInput)
            valid_input = True
        except ValueError:
            valid_input = False

        #Print the tires
        #print(f"Tries: {tries}")

        #If the input is NaA, then ask for another input
        if (valid_input == False):
            print(f"'{guessInput}' is not a number. Please give a number.")
        elif guess_number == secret_number:
            #Won path
            print(f"{Back.GREEN}{Fore.WHITE}You won within {tries} tries, congrats!")
            break
        elif guess_number < secret_number:
            #The guess is below path
            print(f"{guess_number} {Fore.YELLOW}is low. You need a higher number!{Style.NORMAL}\n")
        elif guess_number > secret_number:
            #The guess is above path
            print(f"{guess_number} {Fore.RED}is high. You need a lower number!{Style.NORMAL}\n")
        
        #Show a random motivation message after each several tries
        if (tries % show_message_after_tries == 0):
            print(f"{Fore.MAGENTA}{messages[random.randint(0, len(messages)-1)]}")
    
    print(f"{Fore.RED}You loose! The number was: {secret_number}")

play()