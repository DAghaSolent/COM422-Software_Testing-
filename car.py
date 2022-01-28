class Car:
    
    def __init__(self, current_speed, max_speed, fuel_level):
        self.current_speed = current_speed
        self.max_speed = max_speed
        self.fuel_level = fuel_level

    def accelerate(self, speed_up):
        if self.fuel_level >= 0:
            if self.current_speed + speed_up <= self.max_speed:
                self.current_speed += speed_up
            else:
                self.current_speed = self.max_speed
            self.fuel_level -= 1
    
    def brake(self, speed_down):
        if self.current_speed - speed_down >= 0:
            self.current_speed -= speed_down
        else:
            self.current_speed = 0
    
    def refuel(self, fuel_up):
        if self.fuel_level + fuel_up < 100:
            self.fuel_level += fuel_up
        else:
            self.fuel_level = 100
    