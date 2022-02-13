import task2


def test_exceeding_speed_and_court_summons():
    assert task2.speeding(45, 30) == (True, True)


def test_exceeding_speed_and_no_court_summons():
    assert task2.speeding(39, 30) == (True, False)


def test_abiding_the_law():
    assert task2.speeding(30, 30) == (False, False)