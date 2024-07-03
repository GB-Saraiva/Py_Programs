# Calcule a média aritmética das quatro notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 6, ou a mensagem "reprovado", caso contrário.
import os

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

if media < 6:
    print('Aluno REPROVADO com média {}'.format(media))
else:
    print('Aluno APROVADO com média {}'.format(media))

os.system('pause')