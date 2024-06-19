"""
game logic for Boggle
"""
import random
import string
from pprint import pprint

from model import CheckWordRequest, CheckWordResponse

BogglePlayingField = list[list[str]]

characters: set[str] = set()  # assume we run 1 game in parallel
table: BogglePlayingField = []
guesses: list[str] = []



def guess_word(request: CheckWordRequest) -> CheckWordResponse:
    # ignoring duplicates
    # not checking whether it is a word (could use sowpods.txt)
    correct = set(request.word.upper()).issubset(characters)
    if correct:
        guesses.append(request.word)
    return CheckWordResponse(
        table=table,
        correct=correct,
        guessed=guesses,
    )


def set_playing_field(field: BogglePlayingField) -> None:
    global table  # FIXME: super ugly
    global characters
    characters = set()
    for row in field:
        for char in row:
            characters.add(char)
    table = field


def start_game(xsize: int = 4, ysize: int = 4) -> BogglePlayingField:
    result = []
    for _ in range(ysize):
        result.append(random.choices(string.ascii_uppercase, k=xsize))
    set_playing_field(result)
    return result


if __name__ == "__main__":
    pprint(start_game(9, 9))
