#PSIUDOCODIGO:
#Para cada número de 1 a 10, faça:
#Para cada múltiplo de 1 a 10, faça:
#Calcule o produto do número e do múltiplo.
#Mostre o número, o múltiplo e o produto.
#Fim do loop interno
#Fim do loop externo

#Faça uma programa que mostre
#as tabuadas dos números de 1 a 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {(i*j)}')