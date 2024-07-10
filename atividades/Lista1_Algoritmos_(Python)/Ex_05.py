# Receba dois valores a e b e os escreve com a mensagem: "São pares " ou "São ímpares".
import os

print('Digite dois números e descubra se são pares ou ímpares.')
n1 = int(input('Primerio número: '))
n2 = int(input('Segundo número: '))
if n1 % 2 == 0:
    print('Resultado: {} é PAR e'.format(n1), end=' ')
else:
    print('Resultado: {} é ÍMPAR e'.format(n1), end=' ')
if n2 % 2 == 0:
    print('{} é PAR!'.format(n2))
else:
    print('{} é ÍMPAR!'.format(n2))

os.system('pause')
os.system('cls')