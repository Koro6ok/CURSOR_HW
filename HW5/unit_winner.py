import unittest
from game import TicTacToe


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()


    def test_row(self):

        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.winner(2, 'X'))
        self.game.print_board()
        print('-------------')
        self.game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.assertTrue(self.game.winner(5, 'X'))
        self.game.print_board()
        print('-------------')
        self.game.board = [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X']
        self.assertTrue(self.game.winner(8, 'X'))
        self.game.print_board()
        print('-------------')


    def test_column(self):

        self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game.winner(6, 'X'))
        self.game.print_board()
        print('-------------')
        self.game.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
        self.assertTrue(self.game.winner(7, 'X'))
        self.game.print_board()
        print('-------------')
        self.game.board = [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
        self.assertTrue(self.game.winner(8, 'X'))
        self.game.print_board()
        print('-------------')

    def test_diagonal(self):

        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game.winner(8, 'X'))
        self.game.print_board()
        print('-------------')
        self.game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game.winner(6, 'X'))
        self.game.print_board()
        print('-------------')





if __name__ == '__main__':
    unittest.main()
