# Utilizando Blocos de bytes (chunks)
print('\nUtilizando Blocos de bytes (chunks)')
with open("exemplo.txt", "rb") as f:
    chunk = f.read(1024)  # lê 1 KB por vez
    while chunk:
        print(chunk)
        chunk = f.read(1024)
        