class Dog:
    """
    Class representing Dog.
    Atributes: name - the dog's name
    Method: say() - return what the dog said
    """

    def __init__(self, name):
        self.name = name

    def say(self):
        return f'{self.name}: Гав!'


dog = Dog('Шарик')
print(dog.say())
