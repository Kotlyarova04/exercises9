class TrafficLight:
    permissible_values = ['зеленый', 'желтый', 'красный']

    def __init__(self):
        self.index = 0
        self.current_signal = self.permissible_values[self.index]

    def next_signal(self):
        self.index = (self.index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self.index]

    def __str__(self):
        return f'Текущий свет светафора:{self.current_signal}'


traf = TrafficLight()
print(traf)
traf.next_signal()
print(traf)
