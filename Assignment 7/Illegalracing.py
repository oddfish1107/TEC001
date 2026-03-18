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

container_of_cars = [Car("ABC-1",142),Car("ABC-2",120),Car("ABC-3",150), Car("ABC-4",130),Car("ABC-5",140),Car("ABC-6",130),Car("ABC-7",140),Car("ABC-8",160),Car("ABC-9",95),Car("ABC-10",100)]

for i in range(1,11):
    random_speed = random.randint(150,200)
    registration_number = f"ABC-{i}"
    new_car = Car(registration_number, random_speed)
    container_of_cars.append(new_car)
race = True
while race:
    for car in container_of_cars:
        changing_of_speed = random.randint(-10,15)
        car.accelerate(changing_of_speed)
        car.drive_hours(1)

        if car.traveled_distance >= 10000:
            race = False

for car in container_of_cars:
    print(f"{car.registration_number:<15} | {car.traveled_distance:<12} km | {car.current_speed:<10} km/h | max:{car.maximum_speed:<12} km" )
