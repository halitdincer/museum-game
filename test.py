from state import *
from item import *
from action import * 

# temporary python script to test experimental functions

lobby = Room("Lobby", "Hallway to the home","This is a long description for Lobby", None, None, None, None)

east_wing = Room("East Wing", "East Wing to the home","This is a long description for East Wing", None, None, None, None)

parents_bedroom = Room("Parents Bedroom", "Parents Bedroom to the home","This is a long description for Parents Bedroom", None, None, None, None)
kids_bedroom = Room("Kids Bedroom", "Kids Bedroom to the home","This is a long description for Kids Bedroom", None, None, None, None)
bathroom = Room("Bathroom", "Bathroom to the home","This is a long description for Bathroom", None, None, None, None)

west_wing = Room("West Wing", "West Wing to the home","This is a long description for West Wing", None, None, None, None)

kitchen = Room("Kitchen", "Kitchen to the home","This is a long description for Kitchen", None, None, None, None)
living_room = Room("Living Room", "Living Room to the home","This is a long description for Living Room", None, None, None, None)
dining_room = Room("Dining Room", "Dining Room to the home","This is a long description for Dining Room", None, None, None, None)

lobby.neighbours["east"] = east_wing
lobby.neighbours["west"] = west_wing

east_wing.neighbours["north"] = parents_bedroom
east_wing.neighbours["east"] = kids_bedroom
east_wing.neighbours["south"] = bathroom
east_wing.neighbours["west"] = lobby

parents_bedroom.neighbours["south"] = east_wing

kids_bedroom.neighbours["west"] = east_wing

bathroom.neighbours["north"] = east_wing

west_wing.neighbours["north"] = kitchen
west_wing.neighbours["east"] = lobby
west_wing.neighbours["south"] = living_room
west_wing.neighbours["west"] = dining_room


kitchen.neighbours["south"] = west_wing

dining_room.neighbours["east"] = west_wing

living_room.neighbours["north"] = west_wing

book = Item("Book",lobby)

player = Player("Halit", lobby)






