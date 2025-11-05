from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn

# Lista de alunos
alunos: List[Dict[str, Union[str, float]]] = [
    {"nome": "Lucas",   "nota": 8.5},
    {"nome": "Ana",     "nota": 6.0},
    {"nome": "Rafael",  "nota": 7.5},
    {"nome": "Beatriz", "nota": 9.0},
    {"nome": "Mateus",  "nota": 5.5},
    {"nome": "Carla",   "nota": 7.8},
    {"nome": "João",    "nota": 4.0},
    {"nome": "Lívia",   "nota": 10.0},
    {"nome": "Pedro",   "nota": 7.1},
    {"nome": "Marina",  "nota": 6.9}
]

# Função com List e Dict
def aprovados(lista: List[Dict[str, Union[str, float]]]) -> List[str]:
    return [aluno["nome"] for aluno in lista if aluno["nota"] >= 7]

# Função com Tuple
def melhor_e_pior(lista: List[Dict[str, Union[str, float]]]) -> Tuple[str, str]:
    melhor = max(lista, key=lambda x: x["nota"])["nome"]
    pior = min(lista, key=lambda x: x["nota"])["nome"]
    return (melhor, pior)

# Função com Set
def notas_unicas(lista: List[Dict[str, Union[str, float]]]) -> Set[float]:
    return {aluno["nota"] for aluno in lista}

# Função com Optional
def buscar_aluno(lista: List[Dict[str, Union[str, float]]], nome: str) -> Optional[float]:
    for aluno in lista:
        if aluno["nome"].lower() == nome.lower():
            return aluno["nota"]
    return None

# Função com Union
def formatar_saida(valor: Union[str, float]) -> str:
    return str(valor)

# Função com Any
def imprimir_dado(dado: Any) -> None:
    print(dado)

# Função com NoReturn
def encerrar_app() -> NoReturn:
    raise SystemExit("Programa encerrado.")

# --- Uso das funções ---
print("\nALUNOS APROVADOS")
print(aprovados(alunos))

print("\nMELHOR E O PIOR")
print(melhor_e_pior(alunos))

print("\nNOTAS ÚNICAS")
print(notas_unicas(alunos))

print("\nNOTA DO ...:") 
print("Rafael", buscar_aluno(alunos, "Rafael"))
print("Sílvio (inesxistente):", buscar_aluno(alunos, "Sílvio"))

print("\nFORMATANDO SAÍDA:") 
print(formatar_saida(8.5))
imprimir_dado({"chave": "valor"})

print("\nENCERRAR APP:") 
encerrar_app()