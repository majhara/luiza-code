# Crie o seguinte programa Python no arquivo ex14.py: Colete a idade de duas pessoas.
# E informe se a primeira idade é maior do que a da primeira. Neste aqui, basta responder
# True para informar que a primeira idade é maior que a primeira

from wsgiref import validate


idade_pessoa1 = int(input('Digite a idade da primeira pessoa: '))
idade_pessoa2 = int(input('Digite a idade da segunda pessoa: '))

validacao = False
if idade_pessoa1 > idade_pessoa2:
    validacao = True

print(validacao)