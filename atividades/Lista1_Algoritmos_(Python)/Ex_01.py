# Receba via teclado um número qualquer e exibir o seu sucessor e seu antecessor.
import os

x = int(input('Digite um número: '))
y = x - 1
z = x + 1
print('O antecessor do número {} é {}, e seu sucessor é {}'.format(x, y, z))

os.system('pause')