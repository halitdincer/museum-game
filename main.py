from game import *
from room import *
from item import *
from character import *

game = Game()

game.load()

while True:
    game.update()
    #print(game.p_char.room.items)
    #print(game.p_char.inventory)