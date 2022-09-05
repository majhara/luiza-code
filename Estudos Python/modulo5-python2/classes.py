# Classes
## Uma classe é uma coleção de objetos com características semelhantes. Cada objeto consiste em 2 coisas: características e funcionalidade. No universo da programação, são conhecidas como variáveis e funções.
## São usadas para criar estruturas de dados definidas pelo usuário. As classes definem funções, que identificam os comportamentos e ações que um objeto criado a partir da classe pode realizar com seus dados.
## Uma classe é um modelo de como algo deve ser definido. Na verdade, ele não contém nenhum dado
## Já uma instância é um objeto que é contruído a partir de uma classe que irá conter os valores reais.
## Todas as definições de classe começam com a palavra-chave class, que é seguida pelo nome da classe com primeira letra em maipusculo e dois pontos. Qualquer código recuado abaixo da definição da classe é considerado parte do corpo da classe.

# Construtor
## As propriedades precisam estar dentro de um método __init__(), o que chamamos de construtor
## O método __init__() vai definir o estado inical do objeto atribuindo os valores das propriedades do objeto e é ele que vai inicializar cada nova instância da classe, ex:

class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

## palavra self equivale ao this do Java
## usado para chamar atributps e métodos dentro da própria clase, representadno a instância da classe

## Atributos de classe: podemos criar atributos de classe, que vão possuit o mesmo valor em toda instância que for criada para a classe. Esses atributos são definidos diretamente abaixo da primeira linha da classe, antes do construtor
## No fim, criamos dois objetos e insttanciamos a classe, assim temos 2 cachorros poodles, porém com nomes e idades diferentes

class Cachorro:
    raca = 'poodle'
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
cachorro1 = Cachorro('Rodolfo', 8)
cachorro2 = Cachorro('Mel', 2)

print(cachorro1.nome, cachorro1.idade)
print(cachorro2.nome, cachorro2.idade)
print(Cachorro.raca)