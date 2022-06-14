class Item:
    instances = []

    def __init__(self,name,location):
        self.name = name
        self.location = location

        # Add instance to the class instances
        self.__class__.instances.append(self)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Item: " + self.name
