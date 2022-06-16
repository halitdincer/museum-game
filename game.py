from item import *
from room import *
from character import *

from os.path import exists
import json


class Game:
    
    def __init__(self):
        self.p_char = None
        self.np_chars = []
        self.actions = []
        self.rooms = []
        self.items = []

    def update(self):

        self.p_char.take_turn()

        for npc in self.np_chars: npc.take_turn()

    def load(self):
        
        ans = ''
        while ans != '1' and ans != '2':
            ans = input(" Welcome to Museum Game 1.0 \n 1 - Start a new game \n 2 - Continue from saved game\n")

        if ans == '1':
            file_name = 'new_game_template.json'
        else:
            file_name=''
            while exists(file_name):
                file_name = input("Write your saved game file name?")

        print("Game is loading...")

        f = open(file_name,'r')

        data = json.loads(f.read())

        # load rooms

        for r in data['rooms']:
            self.rooms.append(Room(r['id'],r['name'],r['short_desc'],r['long_desc']))

        for r in data['rooms']:
            room = next((x for x in self.rooms if x.id == r['id']), None)
            room.neighbours['north'] = next((x for x in self.rooms if x.id == r['neighbours']['north']), None)
            room.neighbours['east'] = next((x for x in self.rooms if x.id == r['neighbours']['east']), None)
            room.neighbours['south'] = next((x for x in self.rooms if x.id == r['neighbours']['south']), None)
            room.neighbours['west'] = next((x for x in self.rooms if x.id == r['neighbours']['west']), None)

        # load player
        p_location = next((x for x in self.rooms if x.id == data['player']['location']), None)
        self.p_char = Player(data['player']['name'],p_location)

        # load npcs
        
        for npc in data['np_chars']:
            location = next((x for x in self.rooms if x.id == npc['location']), None)
            npc = NPC(npc['name'],location)
            npc.set_state(StandingState(npc))
            self.np_chars.append(npc)
        
        # load items
        for item in data['items']:
            location = next((x for x in self.rooms if x.id == item['location']), None)
            self.items.append(Item(item['id'],location))

        print("Game loaded !")

    def save(self):
        pass
