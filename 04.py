class Users:
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
        return f'{user.id}, {user.nick_name}, {user.first_name}, {user.last_name}, {user.middle_name}, {user.gender}'


user = Users(12345, 'p_kotlyarova', 'Polina')
user.update()
user.last_name = 'Kotlyarova'
user.update(gender= 'female')
print(user)
