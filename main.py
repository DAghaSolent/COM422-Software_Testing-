from car import Car

ferrari = Car(30, 70, -2)
bmw = Car(30, 70, 30)


#print(f"The Ferrari is doing the speed of {ferrari.current_speed}")
#bmw.refuel()
#print(f"The current fuel level of the bmw is {bmw.fuel_level}")
ferrari.accelerate(43)
print(f"The Ferrari is doing the speed of {ferrari.current_speed}")
#bmw.brake(15)
#print(f"The BMW is doing the speed of {bmw.current_speed}")
ferrari.brake(71)
print(f"The Ferrari is doing the speed of {ferrari.current_speed}")
print()

ferrari.refuel(105)
print(f"The Ferrari fuel level is {ferrari.fuel_level}")