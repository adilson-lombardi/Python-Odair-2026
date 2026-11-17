soma = 0.0

for i in range(10):
    nota = float(input(f"Nota {i + 1}: "))
    soma += nota

media = soma / 107

print()
print(f"Média: {media:.1f}".replace(".", ","))