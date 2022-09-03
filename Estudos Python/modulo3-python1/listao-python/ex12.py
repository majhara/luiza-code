# #Programa Python no arquivo ex12.py: Este programa irá calcular a área de um
# triângulo. Peça para a pessoa informar a medida numérica da base do triângulo, depois
# colete o valor da altura. Apresente o valor da área do triângulo.

base_triangulo = float(input('Digite o valor da base do triangulo em cm: '))
altura_triangulo = float(input('Digite o valor da altura do triângulo em cm: '))
area_triangulo = (base_triangulo * altura_triangulo) / 2
print(f'A área do triângulo é {area_triangulo} cm²')