# Crie o seguinte programa Python no arquivo lista03_02.py: Colete o nome da pessoa, a cidade de nascimento dela, e o ano em que ela nasceu. Depois você irá mostrar os dados coletados em linhas diferentes. E também, deverá informar quantos anos a pessoa terá no ano 2030.

nome = input('Digite seu nome: ')
cidade_nascimento = input('Digite a sua cidade de nascimento:')
ano = int(input('Digite o ano de nascimento:'))

idade_2030 = 2030 - ano

print(nome)
print(cidade_nascimento)
print(ano)
print(f'Em 2030 você terá {idade_2030} anos')
print('===========================================')



          
