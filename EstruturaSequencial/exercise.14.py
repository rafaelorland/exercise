peso = float(input("O peso dos peixes: "))

excesso = peso - 50
multa = excesso * 4

print(f"O peso de exesso foi {excesso:.2f}Kg \nA multa foi de R${multa:.2f}")