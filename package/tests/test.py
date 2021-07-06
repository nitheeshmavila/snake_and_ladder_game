import unittest

from ..src.game import SnakeAndLadderGame

class TestSnakeAndLadderGame(unittest.TestCase):

    def test_player_position_does_not_exceeded_the_board(self):
        board_size = 100
        game = SnakeAndLadderGame(board_size)
        game.add_player("name")
        game.play()
        current_position = game.players[0].position
        self.assertLessEqual(current_position, board_size, "Position exceeded board size")


if __name__ == '__main__':
    unittest.main()