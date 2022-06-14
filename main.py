from game import *
from state import *
from item import *
from action import *

game = Game()

game.load()

while True:
    command = input()
    game.p_char.update(command.split()[0],command.split()[1])

    print(game.p_char.room)
    #print(game.p_char.room.items)
    #print(game.p_char.inventory)