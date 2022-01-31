n = str(input('digite uma frase :')).strip().lower()
print('o nome tem  {} letra A \n A preimeira {} \n A ultima {} posição '.format(n.count('a'),n.find('a')+1,n.rfind('a')+1))