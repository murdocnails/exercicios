#vlr=int(input('digite um numero?'))
#n = str(vlr)
n = int(input('digi um valor com 4 casa?'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('{} analizando '.format(n))
print('{} milhar'.format(m))
print('{} centena'.format(c))
print('{} dezena'.format(d))
print('{} unidade'.format(u))
