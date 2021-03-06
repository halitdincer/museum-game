from item import Item

# Having location class at side in case if we have inventory subclass
class Location:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        pass

class Room(Location):

    def __init__(self,id,name,short_desc,long_desc):
        super().__init__(id,name)
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

    def __str__(self):
        return  "Room: " + self.name
        
