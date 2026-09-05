1. DEFINIÇÃO da função
def dar_boas_vindas():
    print("-"*40)
    print("  Bem-vindo ao nosso aplicativo! 😀")
    print("-"*40)

2. CHAMADA da função
# O código abaixo só será executado se você "chamar" a função pelo nome:

print("Início do programa.")
print('Por favor, aguarde...')
time.sleep(2)  # Simula uma pausa
dar_boas_vindas()  # <-- Isso executa o código dentro da função
print("Meio do programa.")
dar_boas_vindas()  # <-- Podemos chamar de novo!
print("Fim do programa.")2. CHAMADA da função
# O código abaixo só será executado se você "chamar" a função pelo nome:

'nome_da_pessoa' é um PARÂMETRO.
# É uma variável que só existe dentro da função.
def boas_vindas_personalizado(nome_da_pessoa):
    print("-"*40)
    print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)! 😀")
    print("-"*40)

# Ao chamar a função, passamos o ARGUMENTO (o valor)
boas_vindas_personalizado("Maria")
boas_vindas_personalizado("João")

# Esta função recebe dois números e DEVOLVE a soma deles
def somar(a, b):
    resultado = a + b
    return resultado

# Para usar o valor, precisamos guardá-lo em uma variável
soma1 = somar(5, 10)
soma2 = somar(100, 50)

print(f"O primeiro resultado é: {soma1}")
print(f"O segundo resultado é: {soma2}")
print(f"Você pode usar direto no print: {somar(3, 3)}")

# 1. Definimos nossa ferramenta: a função de somar
def somar(a, b):
    """
    Esta função recebe dois números (a e b) e retorna a soma deles.
    (Isso é uma 'docstring', uma boa prática para documentar o que a função faz)
    """
    resultado = a + b
    return resultado

# 2. Parte principal do nosso programa
print("Calculadora de Somas")

# 3. Vamos usar um loop 'for' para tratar dos 3 pares
for i in range(3):
    print(f"\n--- Calculando {i+1}º par ---")
    
    # Pedimos os números ao usuário
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    # Chamamos a função com os números que o usuário digitou
    # e guardamos o valor que ela 'retornou'
    resultado_da_soma = somar(num1, num2)
    
    # Imprimimos o resultado
    print(f"A soma de {num1} + {num2} é = {resultado_da_soma}")

print("\nPrograma finalizado!")

#################################################

import random # Sempre no topo do arquivo!

def gerar_dados(qtd, min_val, max_val):
    """
    Gera uma LISTA de números aleatórios.
    - qtd: quantos números queremos na lista
    - min_val: o valor mínimo (inclusivo)
    - max_val: o valor máximo (inclusivo)
    """
    
    # A estrutura a seguir se chama "List Comprehension". 
    # É um jeito rápido de criar uma lista usando um loop.
    lista_de_dados = [random.randint(min_val, max_val) for _ in range(qtd)]
    
    return lista_de_dados

# Testando a função
dados_aleatorios = gerar_dados(5, 1, 100) # Gera 5 números entre 1 e 100
print(f"Dados gerados: {dados_aleatorios}")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    """Divide a por b, com tratamento para divisão por zero."""
    if b == 0:
        return "Erro (div/0)"
    else:
        # Arredondando para 2 casas decimais para ficar bonito
        return round(a / b, 2)

# --- Nossa Integração ---

QTD_DE_DADOS = 5 # Quantos pares de números queremos testar

print("Gerando dados...")
# Geramos duas listas de dados independentes
lista1 = gerar_dados(QTD_DE_DADOS, 1, 20)
lista2 = gerar_dados(QTD_DE_DADOS, 0, 10) # Permitindo 0 na lista 2 para testar a divisão

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print("-"*40)
print("Iniciando Cálculos (elemento a elemento):")

# Vamos usar um loop 'for' para "caminhar" pelas listas
# A função 'zip' é usada para parear elementos de duas listas
for num1, num2 in zip(lista1, lista2):
    
    print(f"\nPar: ({num1}, {num2})")
    
    # Agora, chamamos nossas funções de cálculo com esses números
    print(f"Soma:       {num1} + {num2} = {somar(num1, num2)}")
    print(f"Subtração:  {num1} - {num2} = {subtrair(num1, num2)}")
    print(f"Multipl.:   {num1} * {num2} = {multiplicar(num1, num2)}")
    print(f"Divisão:    {num1} / {num2} = {dividir(num1, num2)}")

