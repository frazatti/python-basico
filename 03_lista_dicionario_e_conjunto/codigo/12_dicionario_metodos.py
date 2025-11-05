d = {"nome": "Ana", "idade": 25}

# retorna todas as chaves
print(f"d.keys() = {d.keys()} \n")

# retorna todos os valores
print(f"d.values() = {d.values()} \n")

# retorna pares (chave, valor)
print(f"d.items() = {d.items()} \n")

# acesso seguro a uma chave existente
print(f"d.get('nome') = {d.get('nome')} \n")

# acesso seguro a uma chave inexistente com valor padrão
print(f"d.get('cidade', 'SP') = {d.get('cidade', 'SP')} \n")

# remove o item "idade" e retorna o valor
idade = d.pop("idade")
print(f"d.pop('idade') = {idade} \n")

# adiciona ou atualiza pares
d.update({"cidade": "São Paulo", "nome": "Marcos"})
print(f"d após update = {d}\n")
