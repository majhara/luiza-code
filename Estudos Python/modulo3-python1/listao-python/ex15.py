# Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir o valor da conta de energia entre os moradores da casa. No programa eles informam o valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará quanto cada um deverá contribuir com a conta de energia.

valor_conta = float(input('Digite o valor da conta da conta de luz: '))
qtd_moradores = int(input('Digite a quantidade de moradores da casa: '))

preco_por_pessoa = float(valor_conta / qtd_moradores)


print(f'O valor a ser pago por cada morador é {preco_por_pessoa}')
# pesquisar como formatar as casas decimais do float



