#faça um conversor de °c para f°
c = float(input('informe uma temperatura?C°'))
f = 9 * c / 5 + 32
print('°C{:.2f}Convertido em °F {:.2f}'.format(c,f ))
#exta virce e verça
fh= float(input('Informe um °F ? '))
ce= (fh - 32 ) * 5 / 9
print ('°F {:.2f} Convertido em °C {:.2f}'.format(fh,ce))