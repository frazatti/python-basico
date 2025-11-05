carros = ["Fiat", "Chevrolet", "Volkswagen", "Ford", "Honda", "Toyota"]
print(carros)

carros.append("Audi") # adiciona UM item ao final
print('\ncarros.append("Audi"): \n', carros)

carros.extend(["BMW", "Mercedes"]) # adiciona VÁRIOS itens de outra lista
print('\ncarros.extend(["BMW", "Mercedes"]): \n', carros)

carros.insert(2, "Ferrari") # insere item em posição específica
print('\ncarros.insert(2, "Ferrari"): \n', carros)

carros.remove("Ford") # remove a PRIMEIRA ocorrência de um valor
print('\ncarros.remove("Ford"): \n', carros)

carros.pop() # remove o último item e retorna o seu valor
carros.pop(1)  # também pode remover um item de posição específica
print('\ncarros.pop()\ncarros.pop(1): \n', carros)

carros.reverse() # reverse -> inverte a ordem atual
print('\ncarros.reverse(): \n', carros)

carros.sort() # sort -> ordena a lista em ordem alfabética
print('\ncarros.sort(): \n', carros)

carros.sort(reverse=True) # com reverse=True a lista é ordenada de forma decrescente
print('\ncarros.sort(reverse=True): \n', carros)

carros.clear() # clear -> remove TODOS os elementos
print('\ncarros.clear(): \n', carros)
