class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f'Current floor: {self.current_floor}')

    def go_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f'Current floor: {self.current_floor}')

    def go_to(self, floor: int):
        if self.current_floor < floor:
            while self.current_floor < floor:
                self.go_up()
        elif self.current_floor > floor:
            while self.current_floor > floor:
                self.go_down()

if __name__ == '__main__':
    elevator = Elevator(0, 5)
    elevator.go_to(5)
    elevator.go_to(elevator.bottom_floor)