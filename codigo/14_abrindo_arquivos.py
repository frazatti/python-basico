# Abrindo arquivo
print('\nAbrindo arquivo com open():')
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Abrindo arquivo com gerenciador de contexto
# Nesse caso o arquivo é fechado automaticamente
print('\nAbrindo arquivo com gerenciador de conteúdo - with open():')
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print('\n')
