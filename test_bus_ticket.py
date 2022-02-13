import task1


def test_infant_price():
    assert task1.bus_ticket(2) == 0


def test_student_price():
    assert task1.bus_ticket(18) == 2


def test_senior_price():
    assert task1.bus_ticket(66) == 0


def test_normal_bus_ticket():
    assert task1.bus_ticket(34) == 4
