from car import Car


class TestCreation:
    def test_create_car(self):
        ford = Car(30, 70, 10)
        assert ford.current_speed == 30
        assert ford.max_speed == 70
        assert ford.fuel_level == 10

    def test_create_car2(self):
        kia = Car(20, 60, 10)
        assert kia.current_speed == 20
        assert kia.max_speed == 60
        assert kia.fuel_level == 10


class TestMaxSpeed:
    def test_max_speed_car1(self):
        ford = Car(30, 70, 10)
        ford.accelerate(55)
        assert ford.current_speed == 70

    def test_max_speed_car2(self):
        kia = Car(20, 60, 10)
        assert kia.max_speed == 60


class TestFuelLimit:

    def test_fuel_limit_car1(self):
        ford = Car(30, 70, 0)
        ford.accelerate(20)
        assert ford.current_speed == 50

    def test_fuel_limit_car2(self):
        kia = Car(20, 60, 10)
        kia.accelerate(20)
        assert kia.current_speed == 40
        assert kia.fuel_level == 9
