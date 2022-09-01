# Tuplas
## Tupla é uma estrutura parecida com listas, mas com característica de ser imutável. Isso significa que quando uma tupla é criada, não há "possibilidade" de adicionar remover ou alterar seus elementos. Geralmente são utilizadas para adicionar tipos diferentes de informações. Podemos utilizar uma tupla para adicionar, por exemplo, a sigla do estado em uma posição e o nome em outra, tornando-a boa para ser usada quando queremos trabalhar com informações diferentes em uma mesma variável, ex:

tupla = (('MG', 'Minas Gerais'), ('SP', 'São Paulo'), [0, 1, 2, 3])

## É possível inserir uma lista dentro de uma tupla e acessar os elementos

print(f'Remove o ultimo elemento da lista da tupla e retorna: {tupla[2].pop()}')
print(f'Resultado na tela com o objeto lista modificado: {tupla}')

### duvida: por que passou o 2 como argumento na função pop e excluiu o numero 3

