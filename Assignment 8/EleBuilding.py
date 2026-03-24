class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.current_floor = bottom_floor
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moving up ... now at {self.current_floor} floor")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moving down ... now at {self.current_floor} floor")
    def go_to_floor(self, targetfloor):
        while self.current_floor < targetfloor:
            self.floor_up()
        while self.current_floor > targetfloor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(number_of_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)
    def run_elevator(self, desired_elevator, targetfloor ):
        print(f"/n Elevator {desired_elevator} to floor {targetfloor}")
        elevator_order = desired_elevator -1
        selected_elevator = self.elevators[elevator_order]
        selected_elevator.go_to_floor(targetfloor)

building1 = Building(1, 20, 3)
building1.run_elevator(1, 10)
building1.run_elevator(2, 5)
building1.run_elevator(1, 1)
building1.run_elevator(2, 1)
