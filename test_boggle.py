"""
Automated tests for the Facade of the Boggle game
"""
import random

import faker

from boggle import start_game, guess_word, set_playing_field
from model import CheckWordRequest, CheckWordResponse


TEST_PLAYING_FIELD = [
    ["C", "R", "T"],
    ["B", "A", "Z"],
]


def test_start_game():
    # 1. preparations
    # none here
    # 2. call the code we are testing
    game = start_game(xsize=6, ysize=6)
    # 3. check the output
    assert len(game) == 6  # rows
    for i in range(6):
        assert len(game[i]) == 6  # cols


def test_start_game_small():
    game = start_game(xsize=3, ysize=3)
    assert len(game) == 3
    assert len(game[0]) == 3


def test_guess_word():
    set_playing_field(TEST_PLAYING_FIELD)
    cwr = CheckWordRequest(word="cat")
    result = guess_word(cwr)
    assert result.correct


def test_guess_word_typing():
    start_game(xsize=5, ysize=5)
    cwr = CheckWordRequest(word="hello")
    assert type(guess_word(cwr)) == CheckWordResponse


def test_guess_word_random_words():
    start_game(xsize=5, ysize=5)
    f = faker.Faker()
    for _ in range(100):
        cwr = CheckWordRequest(word=f.word())
        assert type(guess_word(cwr)) == CheckWordResponse


# mock function for replacing random.choices
chars = list("XBCOFGTDS")


def my_mock_choices(c, k):
    return [chars.pop(), chars.pop(), chars.pop()]


def test_guess_word_mock():
    """replace the random.choice function by our own"""
    old = random.choices  # save old function
    random.choices = my_mock_choices  # replace with our own function

    game = start_game(xsize=3, ysize=3)
    random.choices = old  # put old function back

    cwr = CheckWordRequest(word="dog")
    result = guess_word(cwr)
    assert result.correct
