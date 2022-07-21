hora = float (input("Quanto vc ganha por hora? "))

horas_trabalhadas = int (input("Quantas horas voce trabalha por mês? "))

salario_bruto = hora * horas_trabalhadas
inss= (8*salario_bruto)/100
sindicato = (5*salario_bruto)/100
ir = (11*salario_bruto)/100
descontos = inss + sindicato + ir 
salario_liquido = salario_bruto - descontos
#pega a hora e as horas trabalhadas e calcula o salario líquido


# aqui vc mostra o valor bruto calculado
print("Voce ganha por mês R$:" + str(salario_bruto))
print("Voce pagou  de INSS R$: " + str(inss))
print("Voce pagou ao sindicato R$: "  + str(sindicato))
print("voce pagou ao imposto de renda R$:" + str(ir))
