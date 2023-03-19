quantia = float(input("Quanto você ganha por hora? "))
hora = float(input("Horas trabalhadas no mês? "))

sb = quantia * hora
ir = sb * 0.11
inss = sb * 0.08
Sidicato = sb * 0.05

sl = sb-(ir+inss+Sidicato)

print(f"""
      
      + Slário Bruto : R$ {sb:.2f}
      - IR (11%) : R$  {ir:.2f}
      - INSS (8%) : R$ {inss:.2f}
      - Sidicato (5%) : R$ {Sidicato:.2f}
      = Salário Liquido : R$ {sl:.2f}
       
      """)