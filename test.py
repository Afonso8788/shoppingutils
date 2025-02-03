from shoppingutils.cart import calculate_total_price
from shoppingutils.discount import apply_discount
from shoppingutils.inventory import check_availability
cart = [
    {'product': 'apple', 'price': 1.50},
    {'product': 'banana', 'price': 1},
    {'product': 'orange', 'price': 1.20}
]
inventory = {
    'apple': 10,
    'banana': 5,
    'orange': 8
}
discount = 10
while True:
    print("""Opção 1 : Calcular o preço total;
          Opção 2 : Aplicar um desconto;
          Opção 3 : Analisar os items
          Opção 4 : Sair""")
    opcao = int(input("Escolhe uma opção."))
    if opcao == 1:
        calculate_total_price(cart)
    if opcao == 2:
        apply_discount(cart, discount)
    if opcao == 3:
        check_availability(cart, inventory)
    if opcao == 4:
        print("Saindo...")
        break
