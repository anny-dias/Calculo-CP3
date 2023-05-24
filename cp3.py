# CP3 - Anny Carolina Andrade Dias - RM:98295

# Código para encontrar o X do vértice, Y do vértice, soma, produto e raízes de uma função de segundo grau com três entradas do usuário

import math

# Receber as entradas do usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcular o valor do vértice (Xv, Yv)
xv = -b / (2*a)
yv = a * xv**2 + b * xv + c

# Calcular o delta
delta = b**2 - 4*a*c

# Verificar se a função possui raízes reais
if delta < 0:
    raizes = "A função não possui raízes reais."
else:
    # Calcular as raízes
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    
    raizes = f"As raízes da função são: x1 = {x1}, x2 = {x2}"

# Calcular a soma e o produto das raízes
soma_raizes = x1 + x2
produto_raizes = x1 * x2

# Imprimir os resultados
print("X do vértice:", xv)
print("Y do vértice:", yv)
print("Soma das raízes:", soma_raizes)
print("Produto das raízes:", produto_raizes)
print(raizes)

# Código para pegar uma lista de valores representando a função de segundo grau e encontrar numericamente todos os valores que podem ser encontrados analiticamente no item 1

import math

# Função para calcular y dado um valor x
def calcular_y(a, b, c, x):
    return a * x**2 + b * x + c

# Receber a lista de valores
valores = input("Digite a lista de valores separados por espaço: ").split()
valores = [float(valor) for valor in valores]

# Calcular os valores que podem ser encontrados analiticamente
resultados = []
for x in valores:
    y = calcular_y(a, b, c, x)
    resultados.append((x, y))

# Imprimir os resultados
print("Valores encontrados analiticamente:")
for x, y in resultados:
    print(f"x = {x}, y = {y}")
