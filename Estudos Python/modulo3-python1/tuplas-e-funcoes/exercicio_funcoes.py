lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1 - 0.1)

#Dada uma lista com n valores, aplicar a função de desconto usando map():
descontos = map(lambda x: desconto(x), lista)
print(list(descontos))

# Retornar os valores maiores que 100, usando filter
maiores = filter(lambda x: x>100, lista)
print(list(maiores))

# Somar todos os valores da lista usando reduce
from functools import reduce
soma = reduce(lambda x, y: x + y, lista, 1)
print(soma)