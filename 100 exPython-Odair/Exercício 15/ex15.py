PrecoUnitario = float(input("Preço Unitário: R$"))
Quantidade = int(input("Quantidade: "))
Frete = float(input("Frete: R$"))
SubTotal = PrecoUnitario * Quantidade
Total = SubTotal + Frete

print(f"Subtotal: R${SubTotal:.2f}")
print(f"Total: R${Total:.2f}")
