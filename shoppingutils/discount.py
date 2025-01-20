def apply_discount(cart, discount):
    price = 0
    for row in cart:
        for linha in row:
            if linha == 'price':
                price = row['price'] + price
    return print(price)