"""
Program Name: Wordle
Version: 2.0
Author: Janick Müller
Description: A Wordle game that can be played in the terminal
"""

import random
import colorama  # Required for colored terminal output: pip install colorama

# Course submission: Introduction to Programming with Python
# Task: Python implementation of the Wordle game

def worte_schreiben():
    """Reads an existing word list and extracts all words that are exactly 5 letters long,
    writing them into a new file called Worte5.txt."""
    with open('Worte.txt', 'r') as datei_worte, open('Worte5.txt', 'w', encoding='utf-8') as datei_worte5:
        for zeile in datei_worte:
            zeile = zeile.strip().upper()
            if len(zeile) == 5:
                datei_worte5.write(zeile + '\n')

def worte_einlesen():
    """Reads a word list where each word must be on a separate line.
    Returns the words as a tuple."""
    with open('Worte5.txt', 'r', encoding='utf-8') as Worte5:
        return tuple(Worte5.readlines())

def wort_wordle(wortliste):
    """Randomly selects a word from the given 'wortliste' and returns it."""
    max_rand = len(wortliste)
    return wortliste[random.randint(0, max_rand - 1)]

def wordle_spielen(wordle_wort):
    """Executes the game logic for Wordle and provides feedback to the player."""
    index = 0

    while index <= 5:
        spieler_wort = str(input(f'{index + 1}. Attempt: ')).upper()
        index_update = spieler_pruefen(spieler_wort)

        # Check if the player has guessed the correct word
        if spieler_wort == wordle_wort[0:5]:
            print('You guessed the word. Congratulations!')
            break

        if index_update == 1:
            # Check the word and provide feedback to the player
            ergebnis = ergebnis_wordle(wordle_wort, spieler_wort)
            print(ergebnis)
        else:
            print('Please enter the word again.')

        index = index + index_update

    if index > 5:
        print(f'The word was not guessed. \nThe solution is: {wordle_wort}')

def spieler_pruefen(spieler_wort):
    """Checks the player's input:
    1. Only letters are allowed
    2. The input must be exactly 5 characters long
    Returns an index increment value indicating if the input is valid."""
    
    index_incr = -1

    # Check if the word has the correct length
    if len(spieler_wort) == 5:
        index_incr = 1
    else:
        print('The word must be exactly 5 letters long.')
        index_incr = 0

    # Check if the word contains only letters
    for zeichen in spieler_wort:
        if not zeichen.isalpha():
            print('Only letters are allowed!')
            index_incr = 0
            break

    return index_incr

def ergebnis_wordle(wordle, spieler):
    liste_gruen = []  # Contains the indices of correct letters at the correct position
    liste_gelb = []   # Contains the indices of letters that exist but are in the wrong position

    # If the same letter is guessed twice but only appears once in the word,
    # both are still marked as "found". This is intentionally done this way.

    # Fill 'liste_gruen'. If the letter is not at the correct position, insert -1.
    # The list MUST have 5 elements.
    for i in range(5):
        if spieler[i] == wordle[i]:
            liste_gruen.append(i)
        else:
            liste_gruen.append(-1)

    # Fill 'liste_gelb' for letters that exist in the wordle word.
    # Otherwise, insert -1. The list MUST have 5 elements.
    for i in range(5):
        liste_gelb.append(wordle.find(spieler[i]))

    # Create the output for the player including correct color coding
    ausgabe = ''

    for i in range(5):
        if i == liste_gruen[i]:
            ausgabe += colorama.Fore.GREEN + spieler[i] + colorama.Fore.RESET
        elif liste_gelb[i] >= 0:
            ausgabe += colorama.Fore.YELLOW + spieler[i] + colorama.Fore.RESET
        else:
            ausgabe += colorama.Fore.LIGHTBLACK_EX + spieler[i] + colorama.Fore.RESET

    return ausgabe

# Main program
worte_schreiben()
wordle_wort = wort_wordle(worte_einlesen())
wordle_spielen(wordle_wort)
