def apply_discount(cart, discount):
    for row in cart:
        for linha in row:
            if linha == 'price':
                row['price'] = row['price']*discount
    return apply_discount(cart,discount)

