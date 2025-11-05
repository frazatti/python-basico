# Crie um programa que receba o nome de 2 arquivos de texto
# e ao final gere um terceiro arquivo unindo o conteúdo 
# dos 2 arquivos de entrada (join)

def juntar_arquivos(arquivo1, arquivo2, destino):
    with open(destino, "w", encoding="utf-8") as out:
        # copia o conteúdo do primeiro arquivo
        with open(arquivo1, "r", encoding="utf-8") as f1:
            for linha in f1:
                out.write(linha)
        # copia o conteúdo do segundo arquivo
        with open(arquivo2, "r", encoding="utf-8") as f2:
            for linha in f2:
                out.write(linha)
    print(f"Arquivos '{arquivo1}' e '{arquivo2}' unidos em '{destino}'.")

# Exemplo de uso
juntar_arquivos("part1.txt", "part2.txt", "join.txt")
