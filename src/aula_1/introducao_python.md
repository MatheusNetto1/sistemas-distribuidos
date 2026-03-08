# 1. Introdução

Python é uma linguagem de programação de alto nível, interpretada e
conhecida por sua simplicidade e legibilidade. É amplamente utilizada em
áreas como:

-   Desenvolvimento web
-   Ciência de dados
-   Automação
-   Inteligência artificial
-   DevOps
-   Desenvolvimento de APIs

Python possui uma sintaxe simples, o que facilita o aprendizado e
permite que programadores foquem mais na lógica do problema.

------------------------------------------------------------------------

# 2. Tipos de Dados

Python possui diversos tipos de dados embutidos.

## Inteiros (int)

``` python
idade = 25
ano = 2025
```

## Float (float)

``` python
altura = 1.80
preco = 19.99
```

## Strings (str)

``` python
nome = "Ana"
mensagem = "Olá mundo"
```

## Booleanos (bool)

``` python
ativo = True
finalizado = False
```

## Listas (list)

Coleções **ordenadas e mutáveis**.

``` python
frutas = ["maçã", "banana", "laranja"]

print(frutas[0])
frutas.append("uva")
```

## Tuplas (tuple)

Coleções **imutáveis**.

``` python
coordenadas = (10, 20)
```

## Sets (set)

Coleções **sem elementos duplicados**.

``` python
numeros = {1,2,3,3,4}
print(numeros)
```

## Dicionários (dict)

Estrutura **chave-valor**.

``` python
usuario = {
    "nome": "Carlos",
    "idade": 30
}

print(usuario["nome"])
```

------------------------------------------------------------------------

# 3. Estruturas de Controle

Permitem controlar o fluxo de execução do programa.

## Condicionais

``` python
idade = 20

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## elif

``` python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")
```

------------------------------------------------------------------------

## Loop For

``` python
for i in range(5):
    print(i)
```

------------------------------------------------------------------------

## Loop While

``` python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

------------------------------------------------------------------------

# 4. Funções

Funções permitem reutilizar código.

``` python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Carlos")
```

## Retorno de valores

``` python
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)
```

## Parâmetros padrão

``` python
def saudacao(nome="Visitante"):
    print("Olá,", nome)
```

------------------------------------------------------------------------

# 5. Módulos e Pacotes

## Módulos

Um módulo é simplesmente um arquivo `.py` contendo código Python.

Exemplo de módulo `matematica.py`:

``` python
def soma(a, b):
    return a + b
```

Importando o módulo:

``` python
import matematica

print(matematica.soma(2, 3))
```

Ou:

``` python
from matematica import soma
```

## Pacotes

Pacotes são diretórios que agrupam vários módulos.

Estrutura:

    meu_pacote/
        __init__.py
        modulo1.py
        modulo2.py

Importação:

``` python
from meu_pacote import modulo1
```

------------------------------------------------------------------------

# 6. Bibliotecas Populares

## NumPy

Biblioteca para computação numérica.

``` python
import numpy as np

array = np.array([1,2,3])
print(array * 2)
```

## Pandas

Usada para manipulação e análise de dados.

``` python
import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "João"],
    "idade": [23, 35, 29]
}

df = pd.DataFrame(dados)
print(df)
```

Leitura de CSV:

``` python
df = pd.read_csv("dados.csv")
print(df.head())
```

## Requests

Biblioteca para fazer requisições HTTP.

``` python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
```

------------------------------------------------------------------------
# 7. Manipulação de Erros e Exceções

Durante a execução de um programa podem ocorrer situações inesperadas, como divisão por zero, arquivos inexistentes ou entrada inválida do usuário. Em Python, esses problemas são chamados de **exceções**.

Para evitar que o programa seja interrompido abruptamente, utilizamos **tratamento de exceções**, permitindo lidar com erros de forma controlada.

## Estrutura básica: try / except

O bloco `try` contém o código que pode gerar erro.  
Se uma exceção ocorrer, o bloco `except` é executado.

```python
try:
    numero = int(input("Digite um número: "))
    print("Número digitado:", numero)
except ValueError:
    print("Entrada inválida. Digite apenas números.")
```

## Capturando exceções específicas

``` python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero")
```

## Capturando diferentes tipos de exceção

``` python
try:
    a = int(input("Digite um número: "))
    resultado = 10 / a
    print(resultado)

except ValueError:
    print("Você precisa digitar um número válido")

except ZeroDivisionError:
    print("Não é possível dividir por zero")
```

Cada tipo de erro possui uma classe de exceção específica.

## Capturando exceções genéricas

Também podemos capturar qualquer erro usando `Exception`.

```python
try:
    x = int("abc")
except Exception as erro:
    print("Ocorreu um erro:", erro)
```

`erro` contém informações sobre a exceção ocorrida.

## Else

O bloco `else` é executado somente se nenhum erro ocorrer.

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido")
else:
    print("Número válido:", numero)
```

## Finally

O bloco `finally` sempre será executado, independentemente de ocorrer erro ou não.

É muito usado para liberar recursos, como fechar arquivos ou conexões.

``` python
try:
    arquivo = open("dados.txt")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    print("Encerrando operação")
```

------------------------------------------------------------------------

# 8. Orientação a Objetos

## Classe

``` python
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
```

Criando objetos:

``` python
pessoa1 = Pessoa("Ana", 25)
pessoa2 = Pessoa("Carlos", 30)

print(pessoa1.nome)
print(pessoa2.idade)
```

## Métodos

``` python
class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print("Olá, meu nome é", self.nome)

p = Pessoa("Maria")
p.apresentar()
```

## Encapsulamento

Encapsulamento significa **proteger os dados do objeto**, controlando como eles são acessados.

Em Python usamos a convenção `_atributo` para indicar que algo é interno.

```python
class Conta:

    def __init__(self, saldo):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def ver_saldo(self):
        return self._saldo
```

## Herança

``` python
class Animal:

    def falar(self):
        print("Som do animal")

class Cachorro(Animal):

    def falar(self):
        print("Au Au")
```

## Polimorfismo

Polimorfismo significa que **objetos diferentes podem responder ao mesmo método de maneiras diferentes.**

```python
class Gato:
    def falar(self):
        print("Miau")

class Cachorro:
    def falar(self):
        print("Au Au")

animais = [Gato(), Cachorro()]

for animal in animais:
    animal.falar()
```

------------------------------------------------------------------------

# 9. List Comprehensions

Permite criar listas de forma concisa.

``` python
numeros = [1,2,3,4]

quadrados = [n**2 for n in numeros]
```

Com condição:

``` python
pares = [n for n in range(10) if n % 2 == 0]
```

------------------------------------------------------------------------

# 10. Estrutura de Projeto Python

Exemplo de organização:

    meu_projeto/

    src/
        main.py
        services.py

    tests/

    requirements.txt
    README.md

------------------------------------------------------------------------

# 11. Boas Práticas (PEP 8)

Python possui um guia oficial de estilo chamado **PEP 8**.

Algumas recomendações:

-   nomes de variáveis em `snake_case`
-   classes em `PascalCase`
-   linhas até \~79 caracteres
-   imports no topo do arquivo

Exemplo:

``` python
def calcular_media(numeros):
    return sum(numeros) / len(numeros)
```

------------------------------------------------------------------------

# 12. Conclusão

Nesta aula vimos:

-   Tipos de dados
-   Estruturas de controle
-   Funções
-   Módulos e pacotes
-   Bibliotecas populares
-   Tratamento de exceções
-   Programação orientada a objetos
-   List comprehensions
-   Estrutura de projetos
-   Boas práticas Python

Esses conceitos formam a base para o desenvolvimento de aplicações mais
complexas em Python.

------------------------------------------------------------------------

# Exercício Prática 1 - Introdução ao Python

## Objetivo

O objetivo deste exercício é aplicar os conceitos básicos de Python abordados na revisão, incluindo variáveis, tipos de dados, estruturas de controle e funções.

## Descrição do Problema

Desenvolva um programa básico em Python que rode no terminal e permita realizar um CRUD (Create, Read, Update, Delete) de alunos em uma faculdade.

Cada aluno deve possuir os seguintes atributos:
- Nome
- E-mail
- Curso (GES, GEC, GEA, etc.)
- Matrícula (gerada automaticamente com base no curso)

A matrícula deve ser composta pelo nome do curso (ou uma abreviação) seguido de um número sequencial. Exemplo:
- Aluno cadastrado no curso de **Engenharia de Software - GES** pode ter a matrícula **GES1**, **GES2**, etc.

## Requisitos

1. **Funções:**
    - O programa deve ser modularizado, com cada funcionalidade implementada em uma função separada.
   
2. **Estrutura de Dados:**
    - O programa deve usar uma lista ou um dicionário para armazenar as informações dos alunos.

3. **Interação com o Usuário:**
    - O programa deve interagir com o usuário através de um menu no terminal, permitindo que ele escolha entre as opções disponíveis.


Boa sorte e mãos à obra!