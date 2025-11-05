print('\nUtilizando stream, lendo linha a linha')
# Utilizando stream, lendo linha a linha
with open("exemplo.txt", "r") as f:
    for linha in f:
        print(linha.strip())
        