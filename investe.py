def main():
    Ativo = ["CDBs", "Acoes", "Fundos Imobiliarios", "Stocks", "Reits"]
    difValor = ""
    percentual = [0] * 5
    aplicacao = [0] * 5
    percentualAtual = [0] * 5
    diferenca = [0] * 5
    somaPercent = 0
    somaAtivo = 0
    maiorNumero = 0

    print("\nINSIRA O VALOR PERCENTUAL\n")

    while somaPercent != 100:
        somaPercent = 0
        for posicao in range(5):
            percentual[posicao] = float(input(f"\nQual a % deseja investir em {Ativo[posicao]}: "))
            somaPercent += percentual[posicao]
        
        if somaPercent != 100:
            print("A soma não corresponde a 100%, insira novamente!\n")

    print("\nINSIRA OS VALORES EM REAL\n")

    for posicao in range(5):
        aplicacao[posicao] = float(input(f"\nQual o valor investido em {Ativo[posicao]}: R$ "))
        somaAtivo += aplicacao[posicao]

    for posicao in range(5):
        percentualAtual[posicao] = (aplicacao[posicao] * 100) / somaAtivo

    print("\nRESULTADO\n")

    for posicao in range(5):
        print(f"\nObjetivo em {Ativo[posicao]}: {percentual[posicao]}%")
        print(f"Valor atual em {Ativo[posicao]} é de: {percentualAtual[posicao]:.2f}%\n")

        if percentual[posicao] > percentualAtual[posicao]:
            diferenca[posicao] = percentual[posicao] - percentualAtual[posicao]
        else:
            diferenca[posicao] = percentualAtual[posicao] - percentual[posicao]

        if diferenca[posicao] > maiorNumero:
            maiorNumero = diferenca[posicao]
            difValor = Ativo[posicao]

    print(f"\nA maior diferença está no Ativo {difValor} com {maiorNumero:.2f}% de diferença\n")

if __name__ == "__main__":
    main()
