mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
mbps = float(input("Digite a velocidade do link de internet (em Mbps): "))

c = mb/(mbps/8)

print(f"{c} segundos")