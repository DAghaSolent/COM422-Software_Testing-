def bus_ticket(age):
    if age < 3:
        return 0
    elif age < 19:
        return 2
    elif age > 65:
        return 0
    else:
        return 4
