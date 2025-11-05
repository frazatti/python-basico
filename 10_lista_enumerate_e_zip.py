planos = ["Plano Junior", "Plano Profissional", "Plano Empresa"]
precos = [50, 70, 90]

# enumerate
for i, p in enumerate(planos):
    print(f"Índice: {i} -> Plano: {p} R$ {precos[i]},00")

print('\n')

# zip
for x, y in zip(planos, precos):
    print(f"Plano: {x} R$ {y}")

print('\n')

# enumerate + zip
for i, (plano, preco) in enumerate(zip(planos, precos), start = 1):
    print(f"{i} - {plano} R$ {preco}")
    