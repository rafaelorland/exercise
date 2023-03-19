# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
nota4 = float(input("Digite a sua quarta nota: "))

media = (nota1+nota2+nota3+nota4)/4

print(f"A média das notas são {media:,.1f}")