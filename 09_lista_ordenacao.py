lojas = ["Magazine Luiza", "Casas Bahia", "Americanas", "Renner", "Havan"]

lojas.sort() # ordena a lista em ordem alfabética crescente
lojas.reverse() # inverte a ordem atual

sorted(lojas, key=len) # ordena pelo tamanho do nome da loja
sorted(lojas, reverse=True) # ordena a lista em ordem alfabética decrescente

sorted(lojas, key=lambda x: x.split()[-1]) # Ordena pelo último nome
