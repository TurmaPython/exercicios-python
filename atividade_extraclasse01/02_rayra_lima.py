notas = []
for n in range(3):
    nota = float(input(f"Digite a nota {n+1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print("A média das notas é:", media)