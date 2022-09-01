#Listas
## Coleção ordenada de valores, onde cada valor é identificado por índices. Em Python, os elementos são separados por vírgulas, dentro de colchetes []. Usada para armazenar diversos itens em uma variável

## Para acessar os dados de uma lista podemos passar o índice como argumento, ex:

lista_frutas = ['Maçã', 'Banana', 'Jaca', 'Melão', 'Abacaxi']
print(f'Estou buscando a fruta: {lista_frutas[2]}')

## Para acessar o último item de uma lista, passa-se como argumento o -1:
print(f'Estou buscando a última fruta da lista: {lista_frutas[-1]}')
## Para saber o tamanho da lista usamos a função len(lista)
print(f'Estou buscando o tamanho da lista: {len(lista_frutas)}')
      
## Python permite indexação negativa, onde você consegue pegar os elementos de trás para frente com o uso de números negativos -1, -2, -3... ex:
print(f'Estou buscando o penultimo elemento da lista: {lista_frutas[-2]}')

## Lista dentro de lista
lista = ['Maçã', ['Banana', 'Jaca'], 'Melão', 'Abacaxi']
sublista = lista[1]
print(f'Acessando a sublista: {sublista}')

## Acessando um item da sublista - duas formas:
print(f'Acessando um item da sublista: {sublista[0]}')
print(f'Acessando um item da sublista: {lista[1][0]}')

## Percorrendo uma lista: A melhor forma é usar um loop
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista_numero_maior_10 = []
lista_append = []
print()
for i in lista:
    if i > 10:
        lista_numero_maior_10.append(i)
print(f'lista:  {lista}')        
print(f'Lista maiores que 10: {lista_numero_maior_10}')
print('Outra forma de fazer: ')

lista_numero_maior_que_10 = [i for i in lista if i > 10]
print(f'Resultado da lista: {lista_numero_maior_que_10}')

## Como manusear uma lista. Para isso, existem vários métodos:
# list.append(x): adiciona um item ao FIM da lista
print('Testando o metodo list.append(16): ')
lista.append(16)
print(lista)

print(f'Testanto o metodo list.append e passando os elementos para outra lista: chamada lista_append')
for i in lista:
    lista_append.append(i+1)

print(f'Append: {lista_append}')

# list.extend(iterable): adiciona todos os itens do iterável ao fim da lista

# list.insert(i, x): insere um item em uma dada posição (i) dada pelo index

lista.insert(8, 'meio')
print(f'Insert: {lista}')

# list.remove(x): remove o primeiro elemento cujo valor for "x"
lista.remove('meio')
print(f'Remove: {lista}')


# list.pop(i): remove o item da posição i da lista e, caso o index não seja especificado, retorna o último elemento:
lista.pop(4)
print(f'Pop: {lista}')
print('Removeu o 4')

# list.index[x[, start[, end]]]: retorna o índice do primeiro elemento cujo valor seja x
print('Testando o metodo list.index[15[, start[, end]]')
#lista.index([15[, start[, end]]])
print(lista)

# list.count(x): retorna o número de vezes que x aparece na lista
print('Testando o método list.count(x):')
print(lista.count(5))

# list.reverse(): reverte os elementos da lista
lista.reverse()
print(f'Reverse: {lista}')

# list.sort(key=nome, reverse=True): ordena os itens da lista
lista.sort()
print(f'Sort: {lista}')

# list.copy(): retorna uma lista com a cópia dos elementos da lista de origem
lista_new = lista.copy()
print(f'Copy: {lista_new}')

# list.clear(): remove tudo da lista
lista_new.clear()
print(f'Clear: {lista_new}')













