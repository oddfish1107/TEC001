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
my_car = Car("ABC-123", 180)


my_car.accelerate(50)
my_car.accelerate(30)



print("Current speed: ", my_car.current_speed)

my_car.accelerate(-200)
print("Final speed: ", my_car.current_speed)
