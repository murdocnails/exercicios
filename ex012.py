#faça um produto que leie um preço de um produto e motre um novo preco com % de desconto
print('Calculador de Desconto')
vl = float(input('Qual o valor do produto ? R$'))
des = float(input('Qual o desconto ?%'))
dct = ( des * vl )/100
n = vl - dct
print('O desconto de {:.1f}% No produto de R${:.2f} é {} o valor descontado \nfoi {:.2f}R$'.format(des, vl, n,dct))

pr= float(input('Digite o preço? R$'))
nv= pr-(5 * pr /100)
print('O valor de {:.2f} sai por {:.2f} com 5% de desconto'.format(pr , nv))