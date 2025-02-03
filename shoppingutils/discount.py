def apply_discount(cart, discount):
    discounted_cart = [{'product': item['product'], 'price' : item['price'] * (1-discount/100)} for item in cart]
    return discounted_cart
