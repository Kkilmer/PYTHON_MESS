#Desenvolva um programa que verifique e mostre
#os números entre 1.000 e 2.000 que, quando
#divididos por 11, produzem o resro igual a 5.

for nm in range(1000, 2001):
    print('-')
    if (nm % 11) == 5:
        print(f'O número é {nm}.')