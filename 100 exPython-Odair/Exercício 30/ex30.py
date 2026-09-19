valor_imovel = float(input("Digite o valor do imóvel: R$ ").replace(',', '.'))
salario = float(input("Digite o seu salário: R$ ").replace(',', '.'))
anos = int(input("Prazo em anos: "))

prestacao = valor_imovel / (anos * 12)
limite = salario * 0.3

if prestacao < limite:
    resultado = "APROVADO"
else:
    resultado = "NEGADO"

print(f"\nPrestação: {prestacao:.2f}.replace('.', ',')\nLimite: {limite:.2f}.replace('.', ',')\nResultado: {resultado}")

input("\nPressione Enter para sair...")
