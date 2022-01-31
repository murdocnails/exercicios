# Crie um programa que leia o nome completo de uma peeoa e mostre:
#>O nome com todas as letras maiúsculas
#>Onome com todas as letras minúsculas.
#>Quantas letras ao todo (sem considerar espaços).
#>Quantas letras tem o primeiro nome.
nome = str(input('Digite o Nome completo :')).strip()
print(nome.upper(),'  Todo maiúsculo !')
print(nome.lower(),'   todo minúsculo !!')
print(len(nome) - nome.count(' '),'total de letras')
d=nome.split()
print('o primeiro nome tem {} letras'.format(nome.find(' ')))
