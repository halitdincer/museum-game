from item import Item

class StateMachine:
    def __init__(self):
        pass

    def update(self, verb, obj):
        pass

class Player(StateMachine):

    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = Room(name+"_inventory","Inventory: " + name,"lorem", "lorem ipsum")

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

    def __init__(self,id,name,short_desc,long_desc):
        self.id = id
        self.name = name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.neighbours = {
                    "north" : None,
                    "east" : None,
                    "south" : None,
                    "west" : None }

    @property
    def items(self):
        return [item for item in Item.instances if item.location == self]

    def update(self, verb, obj):
        if verb == 'move':
            if self.neighbours[obj]:
                return self.neighbours[obj]
            else:
                print("There is no entrance at this way.")
                return self

    def __str__(self):
        return  "Room: " + self.name
        
