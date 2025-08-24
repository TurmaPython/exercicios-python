valor_hora = float(input("Digite o valor da sua hora trabalhada: "))
hora_mes = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = valor_hora * hora_mes

imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

total_descontos = imposto_de_renda + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f"+ Salário Bruto   : R$ {salario_bruto}")
print(f"- Imposto de Renda: R$ {imposto_de_renda}")
print(f"- INSS            : R$ {inss}")
print(f"- Sindicato       : R$ {sindicato}")
print(f"= Salário Líquido : R$ {salario_liquido}")