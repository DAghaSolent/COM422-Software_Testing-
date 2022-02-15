import task3


def test_free_delivery():
    assert task3.delivery_price(8, 120) == "Free Delivery"


def test_5_pound_delivery():
    assert task3.delivery_price(8, 40) == "£5 Delivery Cost"


def test_more_than_10_miles():
    assert task3.delivery_price(11) == "£10 Delivery Cost"


def test_more_than_20_miles():
    assert task3.delivery_price(21) == "£15 Delivery Cost"


def test_more_than_30_miles():
    assert task3.delivery_price(50) == 25


def test_more_than_300_miles():
    assert task3.delivery_price(300) == 150
