import unittest
from unittest.mock import patch
from game import TicTacToe

class TestWinner(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()


    def test_row(self):

        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.winner(2, 'X'))
        self.assertFalse(self.game.winner(3, 'X'))


    def test_column(self):

        self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertFalse(self.game.winner(5, 'X'))


    def test_diagonal(self):

        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game.winner(8, 'X'))
        self.assertFalse(self.game.winner(5, 'X'))


    def test_no_winner(self):
        self.game.board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X']
        self.assertFalse(self.game.winner(8, 'X'))



if __name__ == '__main__':
    unittest.main()
