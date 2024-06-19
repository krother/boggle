from boggle import start_game, guess_word
from model import CheckWordRequest

from pprint import pprint

game = start_game(xsize=6, ysize=6)
pprint(game)

while True:
    word = input("guess a word ")
    req = CheckWordRequest(word=word)
    if guess_word(req).correct:
        print("correct")
    else:
        print("not a correct word")
