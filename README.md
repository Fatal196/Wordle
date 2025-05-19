# Wordle Game in Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)

A simple Wordle clone where the player must guess a five-letter word within six attempts.

Each time the player guesses a letter:
- If the letter is in the word but at the wrong position, it is highlighted **yellow**.
- If the letter is in the correct position, it is highlighted **green**.

After six attempts, the player must have guessed the correct word; otherwise, the game is lost.

This project is designed so that the Python file can be downloaded and executed locally.  
Please make sure to check the `requirements.txt` before running the game.

**Please note that `wordle.py` requires a list of 5-letter words, which is currently only available in German. You can add and/or remove words individually.**


## Installation

Clone the repository:

```bash
git clone https://github.com/Fatal196/Wordle.git
cd Wordle
```
Note: Ensure that the `Worte.txt` file is located in the same directory as `wordle.py`.

Install required Dependencies:
```bash
pip install -r requirements.txt
```
Run the game:
```bash
python wordle.py
```
## Author:
Janick "Fatal196" Müller
