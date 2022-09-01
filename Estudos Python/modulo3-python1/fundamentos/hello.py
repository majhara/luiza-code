#OBS
## Em Python a indentação é obrigatória, isso torna o código mais legível

#VARIÁVEL
##snake_case: separação por underscore em variáveis, funções e métodos
## PascalCase: classes
## SCREAMING_SNAKE_CASE: constantes (convenção para identificar de imetiado uma constante, porém o python admite a modificação do valor da constante)



#Sintaxe lista - nome = [elemento1, elemento2...]
a = [1,2,3,4]

#Métodos para listas

## Método para remover elemento de uma lista passando o elemento como argumento: nome_lista.remove(elemento), ex:
a.remove(1)
## Método para adicionar elemento ao final da lista passando o elemento como argumento: nome_lista.append(elemento), ex:
a.append(5)
## Método para adicionar elemento em determinada posição - passando como argumentos índice e elemento nome_lista.insert(indice, elemento), ex:
a.insert(0, 7)



#Sintaxe Tuplas - uso de ()
b = (1,2,3,4)
# Nelas, não é possível adicionar, alterar ou remover elementos, mas é possível unir duas tuplas
## tupla de 1 elemento - sintaxe: nome = (elemento,)
b2 = (1,)

#Dicionarios
c = {1:'a', 2:'b'}

print(a)



