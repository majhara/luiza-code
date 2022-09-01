# Existem dois tipos de conversão em Python:

## Implicita: o interpretador converte automaticamente um tipo de dado em outro sem qualquer envolvimento do usuário, ex:

a = 15
print(f'A variavel a do tipo: {type(a)}')
#duvida: por que essa formatação?

b = 10.6
a = a + b
print(f'Valor da soma: {a}')

print(f'A variavel a e do tipo: {type(a)}')

## Explícita: Diferente da conversão implícita, esse tipo de conversão é feita manualmente pelo usuário de acordo com seus requisitos, existem várias formas de conversão que se pode fazer nesse tipo, usando as funções do Python:

### int(a,base): converte qualquuer tipo de dado em inteiro. 'Base' especifica a base em que a string está de o tipo de dado for uma string
### float(): converter qualquer tipo de dados em um float
### srt(): usada para converter tuplas em dicionários
### ord(): função usada para converter qualquer caractere em um inteiro
### oct(); converte inteiro em octal
### tuple: converte em um tupla
### Exemplos: 

a = 1
print(type(a))
#output: <class 'int'>
a = str(a)
print(type(a))
#output: <class 'str'>
b = ['a', 'b', 'c', 'd']
print(type(b))
#output: <class 'list'>
b = tuple(b)
print(type(b))
#output: <class 'tuple'>
print(b)
#output: ('a', 'b', 'c', 'd')