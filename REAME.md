# Wordle Game in Python

A simple Wordle clone where the player must guess a five-letter word within six attempts.

Each time the player guesses a letter:
- If the letter is in the word but at the wrong position, it is highlighted **yellow**.
- If the letter is in the correct position, it is highlighted **green**.

After six attempts, the player must have guessed the correct word; otherwise, the game is lost.

This project is designed so that the Python file can be downloaded and executed locally.  
Please make sure to check the `requirements.txt` before running the game.

## Installation

Clone the repository:

```bash
git clone https://github.com/Fatal196/Wordle.git
cd Wordle

## Install required depencies:
pip install -r requirements.txt

## Run the game
python wordle.py
