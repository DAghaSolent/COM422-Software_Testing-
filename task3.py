def delivery_price(miles, value=0):
    if miles <= 10 and value > 100:
        return "Free Delivery"
    elif miles <= 10 and value < 100:
        return "£5 Delivery Cost"
    elif (miles > 10) and (miles < 20):
        return "£10 Delivery Cost"
    elif (miles > 20) and (miles < 30):
        return "£15 Delivery Cost"
    elif miles > 30:
        extra_charge = (miles - 30) * 0.5
        final_delivery_cost = 15 + extra_charge
        return final_delivery_cost