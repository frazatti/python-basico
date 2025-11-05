# lista = ["leão", "girafa", "gorila", "elefante", "rinoceronte"]

lista = list(range(10)) # [0..9]

lista1 = lista[::2] # pares

lista2 = lista.copy()
lista2[3:7] = [30, 40, 50, 60] # substitui faixa

lista3 = lista[::-1] # reverso (cópia)

lista4 = lista.copy()
del lista4[2:5] # remove faixa

print("Lista Original = ", lista)

print("Lista de Pares = ", lista1)
print("Substituíndo Faixa = ", lista2)
print("Valores reversos = ", lista3)
print("Removendo Faixas = ", lista4)
