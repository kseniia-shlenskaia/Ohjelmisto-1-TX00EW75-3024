class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        if not isinstance(change_of_speed, (int, float)):
            print('Wrong input')
            return

        new_speed = self.speed + change_of_speed
        if new_speed > self.maximum_speed:
            self.speed = self.maximum_speed
        elif new_speed < 0:
            self.speed = 0
        else:
            self.speed = new_speed

    def drive(self, hours):
        if not isinstance(hours, (int, float)) or hours < 0:
            print('Wrong input')
            return

        self.travelled_distance += self.speed * hours
