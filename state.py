class StateMachine:
    def __init__(self):
        pass

    def update(self, verb, obj):
        pass

class Player(StateMachine):

    def __init__(self, room):
        self.room = room

    def update(self, verb, obj):
        self.room =  self.room.update(verb,obj)

class State:

    def __init__(self):
        pass

    def update(self, verb, obj): 
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        pass

class Room(State):

    def __init__(self,name,short_desc,long_desc,north,east,south,west):

        self.name = name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.neighbours = {
                    "north" : north,
                    "east" : east,
                    "south" : south,
                    "west" : west }

    def update(self, verb, obj):
        if verb == 'move':
            if self.neighbours[obj]:
                return self.neighbours[obj]
            else:
                print("There is no entrance at this way.")
                return

    def __str__(self):
        return  "Room: " + self.name
        
