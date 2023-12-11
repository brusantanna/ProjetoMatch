def calculadora_financeira():
    print("Bem-vindo à Calculadora Financeira")

    # Validação de Renda
    renda_mensal = validar_renda()

    # Cálculo de Empréstimo
    calcular_emprestimo(renda_mensal)




def validar_renda():

    while True:
        try:
            renda_mensal = float(input("Digite sua renda mensal: R$ "))
            if 0 < renda_mensal < 1000000:  # Definindo o limite de renda conforme necessário
                return renda_mensal
            else:
                print("Sua renda esta incompativel!! A renda deve estar entre 0 e 1.000.000. Tente novamente.")
        except ValueError:
            print("Por favor, digite um valor numérico válido para a renda.")

def calcular_emprestimo(renda_mensal):
    valor_emprestimo = float(input("Digite o valor do empréstimo desejado: R$ "))
    prazo_meses = int(input("Digite o prazo do empréstimo em meses: "))

    # Cálculos
    taxa_juros = 0.05  # Definindo a taxa de juros conforme necessário
    prestacao_mensal = (valor_emprestimo * (1 + taxa_juros)) / prazo_meses
    custo_total = prestacao_mensal * prazo_meses

    # Exibição dos resultados
    print("\nResultado do Cálculo:")
    print("-" * 30)
    print(f"Valor do Empréstimo: R$ {valor_emprestimo:.2f}")
    print(f"Prazo do Empréstimo: {prazo_meses} meses")
    print(f"Taxa de Juros: {taxa_juros * 100:.2f}%")
    print(f"Prestação Mensal: R$ {prestacao_mensal:.2f}")
    print(f"Custo Total do Empréstimo: R$ {custo_total:.2f}")



if __name__ == "__main__":
    calculadora_financeira()