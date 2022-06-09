
class StateMachine:
    def __init__(self):
        self.state = State()

    def on_event(self, event):
        self.state = self.state.on_event(event)

class State:

    def __init__(self):
        pass

    def on_event(self, event): 
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__