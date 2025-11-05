# RESOLVIDO
# Crie uma função que leia um dado arquivo de texto e um termo, ao final retorne o
# número de vezes que a palavra se repete nesse arquivo.

def contar_ocorrencias(nome_arquivo, termo):
    termo = termo.lower()
    total = 0
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:                   # percorre cada linha
            palavras = linha.split()            # quebra em palavras
            for palavra in palavras:
                limpa = palavra.strip(".,!?:;\"'()")  # remove pontuações básicas
                if limpa.lower() == termo:
                    total += 1
    return total



# Exemplo de uso
nome_arquivo = "exemplo.txt"
termo_de_busca = "brasil"
qtd = contar_ocorrencias(nome_arquivo, termo_de_busca)

print(f"'{termo_de_busca}' aparece {qtd} vezes no arquivo {nome_arquivo}")
