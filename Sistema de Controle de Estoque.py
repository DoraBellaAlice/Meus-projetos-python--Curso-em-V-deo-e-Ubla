print("-" * 40)
print("  SISTEMA DE CONTROLE DE ESTOQUE  ")
print("-" * 40)

estoque = {}

while True:
    produto = input("Nome do produto (ou 'sair' para encerrar): ").strip().capitalize()
    if produto.lower() == 'sair':
        break

    quantidade = int(input(f"Quantidade atual de {produto}: "))
    limite_minimo = int(input(f"Quantidade mínima aceitável de {produto}: "))

    # Armazena os dados
    estoque[produto] = {"qtd": quantidade, "min": limite_minimo}
    print("Produto cadastrado com sucesso!\n")

print("\n" + "=" * 40)
print("       RELATÓRIO DE REPOSIÇÃO       ")
print("=" * 40)

# Estrutura de repetição para analisar o estoque
for produto, dados in estoque.items():
    if dados["qtd"] < dados["min"]:
        print(
            f"⚠️ ATENÇÃO: {produto} está com apenas {dados['qtd']} unidades. MÍNIMO É {dados['min']}. Solicitar compra!")
    else:
        print(f"✅ {produto}: {dados['qtd']} unidades. Estoque seguro.")

print("-" * 40)
print("Fim do Relatório. Sistema encerrado.")