# Escrever em um arquivo
with open("exemplo.txt", "w") as f:
    f.write("Primeira linha\n")

# Adicionar conteúdo
with open("exemplo.txt", "a") as f:
    f.write("Segunda linha\n")


# Lendo arquivo
print('\nexemplo.txt ___________________')
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
print('\n_______________________________')
