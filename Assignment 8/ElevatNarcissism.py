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
elevator1 = Elevator(1, 20)
elevator1.go_to_floor(6)
elevator1.go_to_floor(7)
elevator1.go_to_floor(1)


