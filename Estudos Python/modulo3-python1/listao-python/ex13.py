# Crie o seguinte programa Python no arquivo ex13.py: Colete a idade de 3 pessoas e
# mostre a média de suas idades

idade_pessoa1 = int(input('Digite a idade da primeira pessoa: '))
idade_pessoa2 =  int(input('Digite a idade da segunda pessoa: '))
idade_pessoa3 = int(input('Digite a idade da terceira pessoa: '))

media_idades = (idade_pessoa1 + idade_pessoa2 + idade_pessoa3) / 3
print(f'A média de idade das 3 pessoas é: {media_idades}')