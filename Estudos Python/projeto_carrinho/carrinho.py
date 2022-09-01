cart = []
item1 = []
item2 =[]

id_user = input('Insira o id do usuário: ')
id_product = input('Insira o id do produto: ')
price_product = float(input('Insira o preco do produto: '))
quantity_product = int(input('Insira a quantidade do produto: '))

item = [id_user, id_product, price_product, quantity_product]


print(f'Produto: {id_product}, preco unitario: {price_product}, quantidade: {quantity_product}')

def add_item_cart(id_product, price_product, quantity_product):
    cart.append(item)
    print('Item inserido no carrinho!')
    return cart

add_item_cart()

def get_all_items_cart():
    #return todos os itens do carrinho
    pass

def get_item_cart_by_id(id_product):
    filter(lambda x: x >= 0, cart)
    print(list(cart))

def remove_item_by_id(id_product):
    #remover o item do carrinho que tem esse produto
    pass