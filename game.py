class Game:
    
    def __init__(self, p_char):
        self.p_char = p_char
        self.np_chars = []
        self.actions = []
        self.rooms = []
        self.items = []

    def update(self):

        self.p_char.update()

        for npc in self.np_chars: npc.update()

    def load(self):
        pass

    def save(self):
        pass
