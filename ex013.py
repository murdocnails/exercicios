#faça um algorito que leia o salári do funcionário  mostre seu novo salário com 15% de desconto
sl= float(input('Qual o valor do sálario?R%'))
dsc= sl + (sl * 15 /100)
print('O Sálario de {} fica {} com 15 % de aumento'.format(sl,dsc))

#aprendizado extra calculo de dicideo
sal= float(input('Qual o valor do salário?R$'))
dic= float(input('Qual o valor do dicídio?%'))
n= sal * dic /100
au= sal + (sal * dic /100)
print('O salário de {:.2f}R$ com o Aumento de {:.2f}% de dicidío \n Total de {:.2f}R% o Aumento foi de {:.2f}R$'.format(sal, dic, au,n))