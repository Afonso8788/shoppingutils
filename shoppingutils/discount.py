def apply_discount(price, discount):
    discounted_cart = [{'product': item['porduct'], 'price' : item['price']* (1-discount/100) for item in cart]
    return discounted_cart
