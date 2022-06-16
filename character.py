from setuptools import Command
from room import *

class Character:

    def __init__(self, name, room):

        self.name = name
        self.location = room
        self.inventory = Room(name+"_inventory","Inventory: " + name,"lorem", "lorem ipsum")
        self.verb_to_func = {
            'pick_up' : self.pick_up,
            'drop' : self.drop,
            'move' : self.move,
            'status' : self.status,
        }   

    def take_turn(self):
        pass

    # Actions

    def pick_up(self,item_name):
        item = [item for item in self.location.items if item.name == item_name]
        if item :
            print("You picked up: " + item[0].name)
            item[0].location = self.inventory
        else:
            print("There is no item with this name in your room")

    def drop(self,item_name):
        item = [item for item in self.inventory.items if item.name == item_name]
        if item :
            print("You dropped: " + item[0].name)
            item[0].location = self.location
        else:
            print("There is no item with this name in your inventory")
    
    def move(self, direction):
        
        if self.location.neighbours[direction]:
            print("You went to: " + self.location.neighbours[direction].name )
            self.location = self.location.neighbours[direction]
        else:
            print("There is no entrance at this way.")

    def status(self, obj):
        # temporary status function to debug
        print("Player Name: " + self.name)
        print("Player Inventory: " + str(self.inventory.items))

        print("Room Name: " + self.location.name)
        print("Room Items: " + str(self.location.items))


class Player(Character):

    def __init__(self, name, room):
        super().__init__(name,room)

    def take_turn(self):

        print("What is your action?")

        command = input()

        # temporary command parser
        if command :
            verb = command.split()[0]
            object = None
            if len(command.split())>1:
                object = command.split()[1]
                
            if verb in self.verb_to_func.keys() :
                self.verb_to_func[verb](object)
            else:
                print("I didn't understand your command")

class NPC(Character):

    def __init__(self, name, room, state):
        super().__init__(name,room)
        self.state = state

