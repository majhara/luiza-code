# Função
## É uma sequência de comandos que executa uma tarefa, sua principal finalidade é nos ajudar a organizar programas em predações que correspondam a como imaginamos uma solução do problema.
## No Python, além de podermos criar funções, temos a opção de usar funções embutidas que estão disponíveis para nos ajudar a escrever nossos programa e economizar tempo, pois estaremos utilizando funções existentes e não precisaremos criá-las

## Map, Filer e Reduce
### map() - Syntax map(funcao, iteraveis), ex:

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_somada = map(lambda x: x+x, lista)
print(list(lista_somada))

### filter() - Syntax filter(funcao, iteraveis), ex:
pares = filter(lambda x: x%2 == 0, lista)
print(list(pares))

### reduce() - Syntax reduce(funcao, iteraveis)
### aplica uma operação em todos os elementos da lista REDUZINDO a apenas um elemento - necessário importar o módulo functools

from functools import reduce

print('Somar os itens da lista: ')
soma = reduce(lambda x,y: x+y, lista, 0)
print(f'Resultado: ', soma)

## funcao
def foo(value):
    print(f'Ola, esse e o parametro: {value}')
    
foo('LuizaCode')
#Output: Luiza