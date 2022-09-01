# Decorator
## Método para envolver uma função, modificando seu comportamento, ex:

def decorator(funcao):
    def wrapper():
        print("Estou antes da funcao passada como argumento")
        funcao()
        print("Estou depois da execucao da funcao passada como argumento")
    return wrapper

def outra_funcao():
    print("Sou um belo argumento!")
    
funcao_decorada = decorator(outra_funcao)
funcao_decorada()
