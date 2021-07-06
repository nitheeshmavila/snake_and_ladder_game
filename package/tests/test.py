from package.src.models import Dice, Player
import unittest

from ..src.game import SnakeAndLadderGame

class TestSnakeAndLadderGame(unittest.TestCase):

    def test_player_position_does_not_exceeded_the_board(self):
        board_size = 100
        dice = Dice(1, 6)
        game = SnakeAndLadderGame(board_size, dice)
        game.add_player("name")
        game.play()
        current_position = game.players[0].position
        self.assertLessEqual(current_position, board_size, "Position exceeded board size")
    
    def test_snake(self):
        board_size = 100
        dice = Dice(1, 6)
        game = SnakeAndLadderGame(board_size, dice)
        game.add_player("name")
        game.add_snake(14, 7)
        player = game.players[0]
        # moved player to position 10
        player.position = 10
        # dice value is 4
        game.update_player_position(player, 4) 
        self.assertEqual(player.position, 7)


if __name__ == '__main__':
    unittest.main()