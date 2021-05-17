import pytest
from game import TicTacToe


game = TicTacToe()
game.board[4] = "X"



def test_available_moves():
    assert (4 not in game.available_moves())


def test_make_move():
    assert not (game.make_move(4, "x"))
    assert (game.make_move(5, "x"))
    assert (game.board[5] != " ")