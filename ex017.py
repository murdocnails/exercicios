# Faça um programa que leia o comprimento de um cateto oposto
# E do cateto adjacente de um triângulo retângulo , calcule e moste o comprimento
# da hipotenusa.
from math import sqrt
b= float(input('Digite o cateto adjacente :mm '))
c = float (input (' digite o cateto oposto :mm'))
a= sqrt (b) + sqrt(c)
h= sqrt (a)
print('CA {} CO {} = hipotenusa {}'.format(b , c , h))