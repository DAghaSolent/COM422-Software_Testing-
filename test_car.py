from car import Car


class TestCar:

    def test_create_car(self):
        ford = Car(30, 70, 10)
        assert ford.current_speed == 30

    def test_accelerate_car(self):
        ford = Car(30, 70, 10)
        ford.accelerate(35)
        assert ford.current_speed == 65

    def test_max_speed_cap(self):
        ford = Car(30, 70, 10)
        ford.accelerate(55)
        assert ford.current_speed == 70

    def test_fuel_limit(self):
        ford = Car(30, 70, 0)
        ford.accelerate(20)
        assert ford.current_speed == 50
