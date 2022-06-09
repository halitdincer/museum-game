class StateMachine:
    def __init__(self):
        pass

    def update(self, verb, obj):
        pass

class Player(StateMachine):

    def __init__(self, room):
        self.location = Location(room)

    def update(self, verb, obj):
        self.location.update(verb,obj)
    

class Location(StateMachine):
    def __init__(self, room):
        self.room = room
    
    def update(self, verb, obj):
        self.room = self.room.update(verb,obj)


class State:

    def __init__(self):
        pass

    def update(self, verb, obj): 
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

class Room(State):

    def __init__(self,short_desc,long_desc,north,east,south,west):
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.neighbours = [north, east, south, west]

    def update(self, verb, obj):
        if verb == 'move':
            if obj == 'north': 
                return self.neighbours[0]
            elif obj == 'east': 
                return self.neighbours[1]
            elif obj == 'south': 
                return self.neighbours[2]
            elif obj == 'west': 
                return self.neighbours[3]
        
