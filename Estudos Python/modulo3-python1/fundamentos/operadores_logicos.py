print("OPERADORES LÓGICOS: and, or, not")
#and: retorna True se ambas as afirmações forem verdadeiras
#or: retorna True se uma das afirmações forem verdadeiras
#not: inverte o resultado da condição

num1 = 7
num2 = 4

#exemplo operador and:
if num1 > 3 and num2 < 8:
    print('As duas condições são verdadeiras')
# exemplo operador or:
if num1 > 4 or num2 <=8:
    print('Uma ou duas das condições são verdadeiras')

# exemplo operador not:
if not(num1 > 30 and num2 > 8):
    print('Inverte o resultado da condição entre os parâmetros')

print()


# exemplo2 de utilização do operador not:
print("OUTRO EXEMPLO:")
lista = ['a', 'b', 'c', 'd']
print('lista = ', lista) 
if 'c' not in lista:
    print('não tem o c na lista')
else:
    print('tem o c na lista')

