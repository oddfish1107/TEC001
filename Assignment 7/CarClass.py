class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.traveled_distance = 0
my_car = Car("ABC-123", 142)

print(my_car.registration_number)
print(my_car.maximum_speed)
print(my_car.current_speed)
print(my_car.traveled_distance)

