class Bus:

    counter = 0     # number of busses

    def __init__(self, name: str):

        self.name: str = name           # name of bus
        self.index: int = Bus.counter   # index of bus

        Bus.counter = Bus.counter + 1   # increasing bus number, when bus is added