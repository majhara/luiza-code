#Considere as seguintes variáveis:
ovo = 3.4
caju = 12.4

resposta = ovo if 1 > 2 else caju
print(resposta)
#output: 12.4
resposta = ovo if ovo > caju else caju
print(resposta)
#output: 12.4
resposta = ovo if ovo < caju else caju
print(resposta)
#output: 3.4
resposta = 100 if ovo + caju > 15 else 200
print(resposta)
#output: 100
resposta = 100 if ovo == 3 else 0
print(resposta)
#output: 0
