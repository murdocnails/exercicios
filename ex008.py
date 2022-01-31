# escreva um programa que leia um valor
# em metros e exiba convertido em centimetros e milimetros
print('Conversor de metros para centímetros e milímetros !')
m =float(input('Digite um Valor em métros:'))
c = m * 100
mi = m * 1000
print('{} tem {} centímetros!. {} milímetros ...'.format(m , c ,mi))