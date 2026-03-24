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

class Race:
    def __init__(self, name, distance, carlist):
        self.name = name
        self.distance = distance
        self.carlist = carlist
    def hour_passes(self):
        for cars in container_of_cars:
            changing_of_speed = random.randint(-10, 15)
            cars.accelerate(changing_of_speed)
            cars.drive_hours(1)
    def print_status(self):
        for car in container_of_cars:
            print(f"{car.registration_number:<15} | {car.traveled_distance:<12} km | {car.current_speed:<10} km/h | max:{car.maximum_speed:<12} km" )
    def race_finished(self):
        for car in self.carlist:
            if car.traveled_distance >= self.distance:
                return True
        return False
if __name__ == "__main__":
    for i in range(1, 11):
        random_speed = random.randint(150, 200)
        registration_number = f"ABC-{i}"
        new_car = Car(registration_number, random_speed)
        container_of_cars.append(new_car)
    derby = Race("Grand Demolition Derby", 8000, container_of_cars)
    hours = 0
    while not derby.race_finished():
        derby.hour_passes()
        hours = hours + 1

        if hours%10 == 0:
            print(f"Status at hour {hours}")
            derby.print_status()
    print(f"Race finished at hour {hours}")
    derby.print_status()