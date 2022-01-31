# o professor quer sortear 4 alunos para apagar o quadro. faça um programa que leie os nomes
#e escola um
import random
n1= input(' primeiro nome ? ')
n2= input('segundo nome ? ')
n3= input('terceito nome ? ')
n4= input('quarto nome ? ')
l= [n1,n2,n3,n4]
e= random.choice(l)
print('O nome escolhido é {}'.format(e))
