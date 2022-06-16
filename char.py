from state import *

class Character:

    def __init__(self, name, room):

        self.name = name
        self.room = room
        self.inventory = Room(name+"_inventory","Inventory: " + name,"lorem", "lorem ipsum")

    def take_turn(self,verb, object):
        pass

class Player(Character):

    def __init__(self, name, room):
        super().__init__(self,name,room)

class NPC(Character):

    def __init__(self, name, room, state):
        super().__init__(self,name,room)
        self.state = state

