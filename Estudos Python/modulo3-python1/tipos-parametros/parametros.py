#Parâmetros
## São os nomes dados aos atributos que uma função pode receber, são eles que definem quais são os argumentos aceitos por uma função, podendo ou não ter um valor padrão, ex:
## Nesse caso o valor padrão para o parâmetro 'horas' é 220, mas eu posso passar um valor diferente na chamada da função

def calcula_salario(valor, horas=220):
    return valor * horas
print(calcula_salario(35))
print(calcula_salario(35, 110))

## *args e *kwargs são usadas como convenção, podendo receber qualquer outro nome, como *params, **kparams, por exemplo

## *args é usado para passar uma lista de argumentos variáve, sem palavras-chave em forma de tupla, pois a função que recebe não necessariamente saberá quantos argumentos serão passados, ex:

def foo(*args):
    print(f'conteudo: {args}')
    
    for i in args:
        print(i)
foo('Hello', 'Mocas', 'LuizaCode')

## *kwargs: abreviação de keywords arguments. premite passar um dicionário com inúmeras chaves para a função. Isso deixa definido que tal função irá receber tais valores, ex:

def foo(**kwargs):
    print(f'O nome dele(a) e: {kwargs.get("nome")}')
    print(f'A idade dele e: {kwargs.get("idade")}')
    print(f'O pais de residencia e: {kwargs.get("pais")}')
    
foo(nome='Jhon',
    idade='28',
    pais='Brasil')