import math

metros = float(input("O tamanho do quarto em m²: "))

latas = math.ceil(metros / 54)
preco = latas * 80

print(metros/54)
print(f"Quantidades de lata {latas}\nO preço R${preco:.2f}")
