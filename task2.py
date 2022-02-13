def speeding(speed, speed_limit):
    if speed == speed_limit:
        return (False, False)
    elif speed > 10 + speed_limit:
        return (True, True)
    elif speed - speed_limit < 10:
        return (True, False)