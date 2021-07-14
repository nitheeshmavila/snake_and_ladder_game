from collections import deque

from models import Board, Dice, Player, Snake, CrookedDice

class SnakeAndLadderGame:

    def __init__(self, board_size, dice):
        self.players = deque()
        self.board = Board(board_size)
        self.dice = dice
        self.snakes = {} # {start_position: snake_object}

    def add_player(self, name):
        self.players.append(Player(name))
    
    def add_snake(self, start_position, end, type_):
        if start_position <= end:
            return
        if start_position not in self.snakes:
            self.snakes[start_position] = Snake(start_position, end, type_)

    def update_player_position(self, player, dice_value):
        new_position = player.position + dice_value
        # keep the original position if it exceeds the board size
        if new_position > self.board.size:
            new_position = player.position
        print("%s position - %s" %(player.name, new_position))

        # Check if position has snake
        if new_position in self.snakes:
            snake = self.snakes[new_position]
            
            if not snake.dead:
                new_position = snake.end
                print("Snake eat at %s moved to %s" % (snake.start, new_position))
                if snake.type_ == "green":
                    snake.dead = True


        player.position = new_position

    def play(self):
        """ Take a player from the player queue and roll the dice and set position for 10 times"""

        while True:
            player = self.players.popleft()
            dice_value = self.dice.roll()
            print("Dice -> ", dice_value)
            self.update_player_position(player, dice_value)
            new_position = player.position

            if new_position <= self.board.size:
                player.position = new_position
                if player.position == self.board.end:
                    player.won = True
                    print("Player %s won the game" % player.name)
                    self.players.append(player)
                    break
            # add the player to the end of the queue
            self.players.append(player)

