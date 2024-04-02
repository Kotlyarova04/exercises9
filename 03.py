class NotSleeping:
    def __init__(self):
        self.sheep = 0

    def add_sheep(self):
        self.sheep += 1
        print(f'Овечка: {self.sheep}')

    def lost(self):
        self.sheep = 0
        print('Вы сбились')

    def get_count_sheeps(self):
        return self.sheep


person = NotSleeping()
person.add_sheep()
person.add_sheep()
person.lost()
person.add_sheep()
print(person.get_count_sheeps())
