# Driver code

from models import Dice, CrookedDice
from game import SnakeAndLadderGame

board_size = 100

dice_type = int(input("Enter 1 for normal Dice and 2 for Crooked Dice \n"))
if dice_type == 1:
    dice = Dice(1, 6)
elif dice_type == 2:
    dice = CrookedDice(2, 12)
    
game = SnakeAndLadderGame(board_size, dice)
game.add_player("nmn")
game.add_snake(5, 2)
game.add_snake(32, 19)

print("Player initial position ", game.players[0].position)
game.play()
print("Player moved to position ", game.players[0].position)

