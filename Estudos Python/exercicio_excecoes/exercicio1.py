# ===================================================================

                            # Questão 1
# Faça um programa que calcule a raiz quadrada de um número n e trate os casos 
# em que n < 0.
# OBS: Utilize o módulo math para calcular a raiz quadrada.

import math
    
try:
    numero = int(input("Digite o numero: "))
    raiz_quadrada = math.sqrt(numero)
    print(raiz_quadrada)
except ValueError:
    print("Não é possível realizar esse cálculo no conjunto dos números reais")

# ===================================================================

                            # Questão 2
# Faça um programa que calcule a divisão de dois números m e n e trate os casos em
# que n = 0

try:
    m = int(input("Digite o numerador: "))
    n = int(input("Digite o denominador: "))
    divisao = m / n
    print(divisao)
except ZeroDivisionError:
    print("Não é possível dividir um número por 0")


# ===================================================================

                            # Questão 3
# Reescreva esse código de uma forma com que ele seja capaz de tratar a inserção 
# de um caractere por parte do usuário

                            # number = int(input("Digite um número: "))
                            # print("O número digitado foi: ", number)

try:
    number = int(input("Digite um número: "))
    print("O número digitado foi: ", number)
except ValueError:
    print("O sistema suporta apenas caracteres numéricos de 0 a 9")

# ===================================================================

                            # Questão 4
                            
# Tendo em mente que ao executá-lo a exceção NameError é gerada, reescreve o 
# código de forma com que tal exceção seja tratada

                            # number = int(input("Digite um número: "))
                            # print("O número digitado foi: ", n)

try:
    number = int(input("Digite um número: "))
    print("O número digitado foi: ", n)
except NameError:
    print("A variável n não foi definida!")


# ===================================================================

                            # Questão 5

# import mathmatics
# print(math.sqrt(25))

# A exceção gerada é "ModuleNotFoundError: No module named 'mathmatics'", porque o python não foi capaz de encontrar o modulo referido

# ===================================================================

                            # Questão 6
# Observe o seguinte programa:

                # try:
                #     number_1 = float(input("Insira um número: "))
                #     number_2 = float(input("Insira outro número: "))
                #     result = number_1 / number_2
                    
                #     print("Resultado: {:.2f}".format(resultado))
                # except ValueError:
                #     print("Isso não é um número.")
                # except ZeroDivisionError:
                #     print("Divisão por 0 indeterminada.")
                # except:
                #     print("Algo deu errado.")


# Escreva o que será impresso na tela caso o mesmo seja executado com as 
# seguintes entradas (5, 3):  
#Resultado: "Algo deu errado."

# ===================================================================

                            # Questão 7
# Uma colega tentou executar o seguinte programa:

file = open("file.txt", "r")
file_lines = file.readline()
file.close()

# Reescreva o código para que esse erro seja exibido de forma mais clara e 
# amigável.

try: 
    file = open("file.txt", "r")
    file_lines = file.readline()
    file.close()
except FileNotFoundError:
    print("O arquivo ou diretório não foi encontrado!")
    
# ===================================================================

                            # Questão 8
# Observe o seguinte programa:
# Um dos problemas do código acima é que o mesmo além de possuir um erro lógico 
# (execução de um comando de escrita em um arquivo em modo de leitura), abre um
# arquivo e tem a sua execução encerrada sem realizar o close

try: 
    file = open("file.txt", "r")
    file.write("Exemplo de texto.")
except FileNotFoundError:
    print("Arquivo não encontrado!")
except IOError:
    print("Não foi possível escrever no arquivo.")
finally:
    file.close()
    