class Users:
    """Class representing a user of the website
    Atributes:
    required: id,nick_name, first_name
    unnecessary: last_name, middle_name, gender
    Method: update() - sets the value of the atribute"""
    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.id}, {self.nick_name}, {self.first_name}, {self.last_name}, {self.middle_name}, {self.gender}'


user = Users(12345, 'p_kotlyarova', 'Polina')
user.update()
user.last_name = 'Kotlyarova'
user.update(gender= 'female')
print(user)
