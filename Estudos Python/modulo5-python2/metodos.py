# Métodos
## Métodos que estão dentro de uma classe só podem ser chamados se existir uma instância criada para a classe

# Métodos privados:
## São aqueles que não devem ser acessados fora da classe, nem por uma classe base. Para definir um método privado, prefixe o nome dele com um sublinhado duplo "__"

class Cachorro:
    raca = 'poodle'
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def description(self):
        return f"{self.nome} tem {self.idade} anos de idade"
    
    def emite_som(self, som):
        return f"{self.nome} faz {som}"
    
    def __tipo_sanguineo(self):
        return f"O tipo sanguíneo é O"
    
    def busca_tipo_se_responsavel(self, nome):
        if nome == 'Thais':
            return self.__tipo_sanguineo()
    
cachorro1 = Cachorro('Rodolfo', '8').description()
cachorro2 = Cachorro('Mel', '2').emite_som("au au")
cachorro3 = Cachorro('Fred', '2').busca_tipo_se_responsavel("Thais")

# Ocorre um erro porque o método __tipo_sanguineo é privado, portanto não pode ser acessado pelo método busca_tipo_se_responsavel
cachorro4 = Cachorro('Leao', '12').__tipo_sanguineo

print(cachorro1)
print(cachorro2)
print(cachorro3)
print(cachorro4)
