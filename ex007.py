#desenvolva um programa que leia as duas notas de um aluno , calcule e mostre a sua média.
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = float((nota1 + nota2) / 2)
print('A nota primeira foi {} ! A nota segunda {} e a Média das duas são {}'.format(nota1, nota2, media))