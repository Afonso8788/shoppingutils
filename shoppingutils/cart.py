def calculate_total_price(cart):
    total_price = sum(item["price"] for item in cart)
    return total_price
