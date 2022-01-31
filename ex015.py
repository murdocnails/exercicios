#escreva um programa que pergunte a quantidade de km percorridos por um carro
#e a quantidade de dias que ele foi alugado
#calcule o preço a pagar
#sabendo que o dia = 60 e km-0,15
print('Calculadora De aluguéis de Carros !!!')
du= int(input('Quantos dias foi usado ? '))
kmr= float(input('Quantos km Percorridos ? '))
d= float(input('Qual Carro foi usado \n Importado R$100 \n popular R$60 ? '))                 #variavel diperente tipo de carro
km = 0.15
print('Uso {} Dias Percorreu {}km Pagara R${}'.format(du,kmr,(du * d) + (kmr * km),))