from setuptools import Command
from room import *

class Character:

    def __init__(self, game, name, room):

        self.game = game
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
            item[0].location = self.inventory
            self.game.log(self.name + " pick up " + item_name)

    def drop(self,item_name):
        item = [item for item in self.inventory.items if item.name == item_name]
        if item :
            item[0].location = self.location
            self.game.log(self.name + " drop " + item_name)
    
    def move(self, direction):
        
        if self.location.neighbours[direction]:
            self.location = self.location.neighbours[direction]
            self.game.log(self.name + " move " + direction)

    def status(self, obj):
        # temporary status function to debug
        print("Player Name: " + self.name)
        print("Player Inventory: " + str(self.inventory.items))

        print("Room Name: " + self.location.name)
        print("Room Items: " + str(self.location.items))


class Player(Character):

    # basic narrate
    def narrate(self,verb,object):
        if verb == 'pick_up':
            print("You picked up the " + object)
        elif verb == 'drop':
            print("You dropped the " + object)
        elif verb == 'move':
            print(" - You enter the " + self.location.name + " - ")
            #print("You saw " + str(self.location.np_chars) + " in the room.")
            if self.location.items:
                print("There is " + ','.join([item.name for item in self.location.items]) + " on the floor.")

    def take_turn(self):

        command = input("> ")

        # temporary command parser
        if command :
            verb = command.split()[0]
            object = None
            if len(command.split())>1:
                object = command.split()[1]
                
            if verb in self.verb_to_func.keys() :
                self.verb_to_func[verb](object)
                self.narrate(verb,object)
            else:
                print("I didn't understand your command")

class NPC(Character):

    def __init__(self,game, name, room):
        super().__init__(game, name, room)
        self.state = TravelState(self,'parents_bedroom')

    def set_state(self, state):
        self.state = state      

    def take_turn(self):
        if self.state:
            self.state.take_turn() 

class State:

    def __init__(self, character):
        self.character = character

class StandingState(State):

    def take_turn(self):
        self.character.status(None)

class TravelState(State):

    def __init__(self,character,destination):
        super().__init__(character)
        self.destination = destination

    def find_direction(self, room, destination):
        visited = []
        queue = []

        visited.append(room)

        for direction in room.neighbours.keys():
            if room.neighbours[direction]:
                queue.append({'self' : room.neighbours[direction],'direction' : direction})

        while queue:

            s = queue.pop(0) 

            if s['self'].id == destination:
                return s['direction']

            for neighbour in s['self'].neighbours.values():
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append({'self' : neighbour,'direction' : s['direction']})
        
        return 'nothing'

    def take_turn(self):
        self.character.move(self.find_direction(self.character.location,self.destination))
        if self.character.location.id == self.destination:
            self.character.set_state(StandingState(self.character))
