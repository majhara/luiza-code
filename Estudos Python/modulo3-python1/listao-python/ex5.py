# 5) Resolva estes problemas em Python, guardando os valores e seus resultados em variáveis diferentes:

## Calcule a área de um quadrado cujo lado seja 2 cm.

lado_quadrado = 2.0
area = lado_quadrado * lado_quadrado
print(f"A área do quadrado é igual a: {area} cm")
## Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela.
preco_mala = 120.00
preco_desconto = preco_mala - (preco_mala * 0.05)
print(f"O valor da mala com desconto é: {preco_desconto}")

## Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem será 200 Km. Quantas horas irá demorar a viagem.
velocidade_media = 100
distancia = 200
tempo = distancia / velocidade_media
print(f"O tempo para percorrer 200km a 100km/h é {tempo} horas")
print()
## João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e sua média.
qtd_joao = 2
qtd_maria = 3
qtd_sofia = 1
total = qtd_joao + qtd_maria + qtd_sofia
media_pirulitos = total / 3
print(f"O total de pirulitos é {total} e a media é {media_pirulitos}")

## Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a verificação se a idade de Davi é maior que a idade de sua irmã.
idade_davi = 13
idade_irma = 7

if idade_davi > idade_irma:
    print("Davi é mais velho")
else: 
    print("a irmã de Davi é mais velha")
