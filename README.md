# Repositório de Python Básico

Este repositório contém exemplos de código e desafios para o aprendizado dos conceitos fundamentais da linguagem Python. O conteúdo é estruturado de forma modular, progredindo do básico ao avançado.

## 🚀 Conteúdo

O repositório está organizado nos seguintes módulos:

### 01. Conceitos Básicos
* **Código:**
    * `01_variaveis.py`: Demonstração de tipos de variáveis e verificação de uso de memória com `sys.getsizeof`.
    * `02_funcoes.py`: Exemplo de definição e uso de funções básicas para operações matemáticas.
    * `03_condicoes.py`: Uso de estruturas condicionais `if`, `elif` e `else` com entrada do usuário.
    * `04_lacos.py`: Exemplos de laços `for`, ordenação de listas de dicionários com `sorted` e `lambda`, e uso de `enumerate`.
* **Desafios:**
    * `D01_caracteres_unicos.py`: Desafio para encontrar caracteres únicos em uma string.
    * `D02_busca_no_texto.py`: Desafio para implementar uma busca de termo em um texto, caractere por caractere.

### 02. Tipagem
* **Código:**
    * `05_typing.py`: Introdução ao sistema de *type hints* (anotações de tipo) do Python.
* **Desafios:**
    * `D03_lista_pares.py`
    * `D04_calculos_lista.py`
    * `D05_numeros_duplicados.py`
    * `D06_interseccao.py`
    * `D07_ordenacao_lista_numerica.py`
    * `D08_uniao_ordenada_de_listas.py`

### 03. Lista, Dicionário e Conjunto
* **Código:**
    * `06_lista_manipulacao_basica.py`: Manipulação de listas usando fatiamento (slicing).
    * `07_lista_funcoes.py`: Exemplos de funções built-in para listas (ex: `len`, `sum`, `min`, `max`).
    * `08_lista_metodos.py`: Demonstração dos principais métodos de listas (`append`, `extend`, `pop`, `sort`, `reverse`, etc.).
    * `09_lista_ordenacao.py`: Formas de ordenação usando o método `sort()` e a função `sorted()` com `key`.
    * `10_lista_enumerate_e_zip.py`: Uso de `enumerate` e `zip` para iterar sobre listas.
    * `11_dicionario_manipulacao_basica.py`: Criação, acesso e modificação de dicionários.
    * `12_dicionario_metodos.py`: Métodos de dicionário como `.keys()`, `.values()`, `.items()`, `.get()`.
    * `13_conjunto.py`: Introdução à estrutura de dados `set` (conjunto) e suas operações (`union`, `intersection`, `difference`).
* **Desafios:**
    * `D16_cadastro_clientes.py`: Desafio de implementação de um cadastro.

### 04. Arquivos e Streams
* **Código:**
    * `14_abrindo_arquivos.py`
    * `15_escrevendo_em_arquivo.py`
    * `16_streams.py`
    * `17_streams_utilizando_chunks.py`
    * `18_copiando_imagem.py`
* **Desafios:**
    * `D09_numero_de_linhas.py`
    * `D10_busca_no_arquivo.py`
    * `D11_juntar_arquivos.py`

### 05. API (Flask e FastAPI)
* **Código:**
    * `19_flask.py`: Exemplo de uma API básica usando Flask.
    * `20_fastAPI.py`: Exemplo de uma API básica usando FastAPI.
    * `index.html`: Arquivo HTML simples para frontend.
* **Desafios:**
    * `D12_minha_api.py`: Desafio para criar uma API.

### 06. Banco de Dados com Python
* **Código:**
    * `21_criando_crud_api-frontend.html`: Frontend para interagir com a API de CRUD.
    * `22_criando_crud_api.py`: Backend da API de CRUD.
    * `23_criando_crud_console.py`: Exemplo de CRUD via console.
* **Desafios:**
    * `D13_conectando_SQLite.py`: Desafio de conexão com SQLite.
    * `D14_conectando_MySQL.py`: Desafio de conexão com MySQL.
    * `D15_conectando_SQLAlchemy_SQLite.py`: Desafio de conexão com SQLite usando SQLAlchemy (ORM).

---

## 🏁 Como Começar

Siga este guia para baixar e executar os exemplos de código no seu computador usando o Visual Studio Code.

### Pré-requisitos

* **Python:** É essencial ter o Python instalado. Baixe em [python.org](https://www.python.org/downloads/).
    * *Dica:* Durante a instalação no Windows, marque a opção "Add Python to PATH".
* **Visual Studio Code:** Nosso editor de código. Baixe em [code.visualstudio.com](https://code.visualstudio.com/).

### Passo a Passo

**1. Baixe o Código**

* Acesse o link do repositório: [https://github.com/frazatti/python-basico](https://github.com/frazatti/python-basico)
* Clique no botão verde **`< > Code`** e selecione **"Download ZIP"**.
* Extraia o arquivo `.zip` em uma pasta de sua preferência (ex: `Meus Documentos/Projetos`).

**2. Configure o VS Code**

* Abra o VS Code.
* Instale a extensão **Python** da Microsoft. (Vá no menu "Extensões" na barra lateral, procure por `Python` e clique em "Instalar").
* Abra a pasta do projeto: Vá em `File > Open Folder...` e selecione a pasta que você extraiu (ex: `python-basico-main` ou `Python-Basico`).
* Se o VS Code perguntar, clique em "Yes, I trust the authors" (Sim, eu confio nos autores).

**3. Execute um Arquivo**

* Na barra lateral "Explorador" (ícone de arquivos), navegue pela estrutura de pastas.
    * *Exemplo:* `01_conceitos_basicos` -> `codigo`
* Clique em um arquivo, como `03_condicoes.py`, para abri-lo.
* Clique no **ícone de "Play" (▶)** no canto superior direito do editor.
* O código será executado no painel **"Terminal"** na parte inferior.

> **Nota:** Alguns scripts, como o `03_condicoes.py`, pedem uma entrada do usuário (`input()`). Você deve **clicar dentro do Terminal** e digitar sua resposta, depois pressionar **Enter** para o script continuar.
