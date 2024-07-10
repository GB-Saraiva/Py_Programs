# Leia dois valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".
import os

print('Descubra se dois números são múltiplos ou não.')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

result = int(n1 % n2)

if result == 0:
    print('SIM os números {} e {} são múltiplos!'.format(n1, n2))
else:
    print('NÃO os números {} e {} não são múltiplos'.format(n1, n2))

os.system('pause')
os.system('cls')