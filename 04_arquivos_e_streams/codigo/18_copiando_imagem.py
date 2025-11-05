with open("origem.png", "rb") as origem, open("copia.png", "wb") as destino:
    destino.write(origem.read())
    