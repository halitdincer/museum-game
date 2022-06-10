from state import Player
from item import Item

def pick_up(player,item):
    if item.location == player.room :
        item.location = player.inventory

