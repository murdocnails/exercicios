#faça um programa que leia a altura e o comprimento de uma parede
#e calcule sua area e a quantidade de tinta nescessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2 m²
alt = float(input('digite a area de sua a atura da parede?m '))#altura
larg= float(input('digite o largura da parete?m '))#comprimeno
ar= (alt * larg)
tin= ar / 2
print('A parede tem  {:.2f}x{:.2f} tem {:.2f} m² Precisa de {:.2f}L de tinta'.format(alt, larg ,ar , tin))