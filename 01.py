class Dog:
    """Return what the Dog say."""

    def __init__(self, name):
        self.name = name

    def say(self):
        return f'{self.name}: Гав!'


dog = Dog('Шарик')
print(dog.say())
