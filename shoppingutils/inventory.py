def check_availability(cart, inventory):
    for item in cart:
        if item["product"] not in inventory or inventory[item["product"]] < 1:
            return False
    return True