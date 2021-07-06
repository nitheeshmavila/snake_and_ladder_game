from collections import deque

from models import Board, Dice, Player

class SnakeAndLadderGame:

    def __init__(self, board_size):
        self.players = deque()
        self.board = Board(board_size)
        self.dice = Dice(1, 6)
    
    def add_player(self, name):
        self.players.append(Player(name))

    def play(self):
        """ Take a player from the player queue and roll the dice and set position"""
        
        player = self.players.popleft()
        dice_value = self.dice.roll()
        new_position = player.position + dice_value
        
        if new_position > self.board.size:
            # No changes in position
            pass
        else:
            player.position = new_position
            if player.position == self.board.end:
                player.won = True
        # add the player to the end of the queue
        self.players.append(player)
        

# Driver code
board_size = 100
game = SnakeAndLadderGame(board_size)
game.add_player("name")
print("Player initial position ", game.players[0].position)
game.play()
print("Player moved to position ", game.players[0].position)
