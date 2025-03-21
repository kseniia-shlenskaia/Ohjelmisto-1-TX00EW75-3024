class Elevator:
    def __init__(self, bottom_floor, top_floor):
        if bottom_floor > top_floor:
            print('Wrong input. The bottom floor cannot be higher than the top floor')

        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def go_to_floor(self, new_floor):
        if not (self.bottom_floor <= new_floor <= self.top_floor):
            print(f'Wrong input. The elevator cannot go below the bottom floor {self.bottom_floor} or above the top floor {self.top_floor}')
            return

        if new_floor == self.floor:
            print(f"The elevator is already on floor number {self.floor}")
            return

        while new_floor != self.floor:
            if new_floor > self.floor:
                self.floor_up()
            elif new_floor < self.floor:
                self.floor_down()

    def floor_up(self):
        self.floor += 1
        print(f"The elevator is on floor number {self.floor}")

    def floor_down(self):
        self.floor -= 1
        print(f"The elevator is on floor number {self.floor}")

h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)
