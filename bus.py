class Bus:

    def __init__(self, speed, capacity, maxSpeed, passengers):
        self.speed = speed
        self.capacity = capacity
        self.maxSpeed = maxSpeed
        self.passengers = passengers or []
        self.seats = {f'Seat {i}': None for i in range(1, capacity + 1)}

    def boarding(self, passengers):
        if isinstance(passengers, list):
            if len(passengers) > 0:
                if self.passengers + len(passengers) <= self.capacity:
                    self.passengers += len(passengers)
                    print(
                        f'В автобус было посажено {len(passengers)} пассажиров: {", ".join(passengers)}')
                else:
                    print('Недостаточно мест для пассажиров')
            else:
                print(
                    'Список пассажиров должен содержать хотя бы одного человека.')
        else:
            print('Пожалуйста, передавайте список пассажиров.')

    def disembarkation(self, count):
        if count > 0:
            self.passengers = max(0, self.passengers - count)
            print(f'Из автобуса было высажено {count} Пассажиров')
        else:
            print(
                'Количество пассажиров для высадки должно быть положительным.')

    def speed_up(self, count):
        if count > 0:
            if self.maxSpeed > self.speed + count:
                self.speed += count
            print(f'Скорость автобуса была увеличина на {count}, текущая скорость: {self.speed}')

    def speed_down(self, count):
        if count > 0:
            if self.maxSpeed > self.speed - count:
                self.speed -= count
            print(f'Скорость автобуса была снижена на {count}, текущая скорость: {self.speed}')

    def seat_passenger(self, passenger_name):
        for seat, occupant in self.seats.items():
            if occupant is None:
                self.seats[seat] = passenger_name
                break

    def unseat_passenger(self, passenger_name):
        for seat, occupant in self.seats.items():
            if occupant == passenger_name:
                self.seats[seat] = None
                break

    def __contains__(self, passenger_name):
        return passenger_name in self.passengers

    def __iadd__(self, passenger_name):
        self.boarding([passenger_name])
        return self

    def __isub__(self, passenger_name):
        self.disembarkation(passenger_name)
        return self


bus = Bus(60, 55, 100, 13)
bus.boarding(['Bob', "Jhon", "Ivan"])
bus += 'Alice'
bus.boarding(2)
bus -= 1
bus.disembarkation(2)
bus.speed_up(20)
bus.speed_down(10)
