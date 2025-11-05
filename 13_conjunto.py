# Criando um conjunto
frutas = {"maçã", "banana", "laranja", "maçã"}
vazio = set()


# Operações
impares = {1, 3, 5, 7}
pares = {2, 4, 6, 8}

union = impares.union(pares) # União -> {1, 2, 3, 4, 5, 6, 7, 8}
intersection = impares.intersection(pares) # Interseção -> set()   (nenhum elemento em comum)
difference = impares.difference(pares) # Diferença -> {1, 3, 5, 7}   (apenas os ímpares)
symmetric_difference = impares.symmetric_difference(pares) # Diferença simétrica -> {1, 2, 3, 4, 5, 6, 7, 8} 

# Imprimindo Valores
print("\n")
print(f"impares = {impares}")
print(f"pares = {pares}")
print("\n")
print(f"impares.union(pares) = {union}")
print(f"impares.intersection(pares) = {intersection}")
print(f"impares.difference(pares) = {difference}")
print(f"impares.symmetric_difference(pares) = {symmetric_difference}")
print("\n")
