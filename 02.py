class NotSleeping:
    def __init__(self):
        self.sheep = 0

    def add_sheep(self):
        self.sheep += 1
        return self.sheep


person = NotSleeping()
person.add_sheep()
print(person.add_sheep())

