#List comprehension
## Na PEP-202 foi concebida a forma mais concisa de criar e manipular listas, através de List Comprehension
### Forma concisa de criar uma lista
lista = [i for i in range(10) if i%2 == 0]
print(lista)

lista_nova = [['Banana', 'Maca'], ['Melao', 'Pera']]
#for x in lista_nova:
    #print(x)
    
#for index, elemento in enumerate(lista):
    #print(index)
    
print(lista_nova[0][0])
