# faça um programa que digite um angulo e ele calcule o sen cos tan desse angulo
import math
a= int(input('Digite um Ângulo: °'))
s= math.sin(math.radians(a))
c= math.cos(math.radians(a))
t= math.tan(math.radians(a))

print('o Ângulo {}°\n seno {:.4f}° \n consseno {:.3f}° \n tangente {:.4f}°'.format(a ,s ,c ,t ))