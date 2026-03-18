import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self, change_speed):
        self.current_speed = self.current_speed + change_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive_hours(self, hours):
        distant_warp = self.current_speed * hours
        self.traveled_distance = self.traveled_distance + distant_warp
my_car = Car("ABC-123", 180)

my_car.current_speed = 60
my_car.traveled_distance = 2000

my_car.drive_hours(1.5)


print(f"Distance: {my_car.traveled_distance} km")
