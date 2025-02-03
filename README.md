Shoppingutils:
Um ficheiro shoppingutils que pode tanto aplicar um desconto ao determinado número de compras, ou avaliar se um produto está ou não está, ou calcular o preço final das compras.
Uso:
from shoppingutils.cart import calculate_total_price
ou
from shoppingutils import cart
cart.calculate_total_price

calculate_total_price (cart)
Onde cart é uma lista de dicionários.

Recebe uma lista de itens no carrinho de compras e retorna o preço total da compra. Cada item do carrinho de compras é representado por um dicionário com as seguintes chaves: product (nome do produto) e price (preço do produto).

from shoppingutils.discount import apply_discount
ou
from shoppingutils import discount
discount.apply_discount

apply_discount (cart, discount)
Onde cart é uma lista de dicionários e o discount é a percentagem de desconto.

Recebe uma lista de itens no carrinho de compras e um desconto percentual (que é sempre o mesmo para todos os produtos) como parâmetros. A função calcula o desconto aplicado a cada item do carrinho de compras e retorna uma nova lista de itens com os preços atualizados.

from shoppingutils.inventory import check_availability
ou
from shoppingutils import inventory
inventory.check_availability

check_availability (cart, inventory)
Onde cart é uma lista de dicionários e o inventory é um dicionário.

Recebe uma lista de itens no carrinho de compras e um dicionário representando o inventário do supermercado. O inventário é um dicionário em que as chaves são os nomes dos produtos e os valores são as quantidades disponíveis em stock. A função verifica se todos os itens do carrinho estão disponíveis em quantidade suficiente e retorna True se estiverem disponíveis ou False caso contrário.
