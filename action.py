from room import Player
from item import Item

def pick_up(player,item):
    if item.location == player.room :
        item.location = player.inventory

def drop(player,item):
    if item.location == player.inventory:
        item.location = player.room
