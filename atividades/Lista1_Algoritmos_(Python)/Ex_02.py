# Receba via teclado um número inteiro qualquer e exiba se ele é positivo, negativo ou zero.
import os

x = int(input('Digite um número para descobrir se ele é positivo, negativo ou igual a zero: '))

if x > 0:
    print('{} é um número positivo'.format(x))
elif x < 0:
    print('{} é um número negativo'.format(x))
else:
    print('{} é nulo, zero(0)'.format(x))

os.system('pause')