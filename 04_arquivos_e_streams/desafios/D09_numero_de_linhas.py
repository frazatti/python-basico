# RESOLVIDO !!
# Dado um arquivo de texto, escreva um programa que conte e exiba 
# o número total de linhas.

nome_arquivo = "exemplo.txt"

# Resposta 1 - Utilizando readLines
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    total1 = len(linhas)
    print(f"'{nome_arquivo}' possui {total1} linhas.")

# Resposta 2 - Utilizando for
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    total2 = 0
    for _ in arquivo:   # percorre cada linha do arquivo
        total2 += 1
print(f"'{nome_arquivo}' possui {total2} linhas.")
