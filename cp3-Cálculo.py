# CP3 - Anny Carolina Andrade Dias - RM:98295

# Código para encontrar o X do vértice, Y do vértice, soma, produto e raízes de uma função de segundo grau com três entradas do usuário

import math

# Receber as entradas do usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

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

# Calcular o valor do vértice (Xv, Yv)
xv = -b / (2*a)
yv = - math.sqrt(delta) / (4*a)

# Imprimir os resultados
print("X do vértice:", xv)
print("Y do vértice:", yv)
print("Soma das raízes:", soma_raizes)
print("Produto das raízes:", produto_raizes)
print(raizes)

# Código para pegar uma lista de valores representando a função de segundo grau e numericamente encontra todos os valores que voce pode encontrar analiticamente

def grafico_funcao(a,b,c):
    i = -100
    x = []
    y = []
    while i < 10:
        x.append(i)
        f = a * i ** 2 + b * i + c
        y.append(f)
        i += 1

    print (x)
    print(y)

print("Gráfico da função:") 
grafico_funcao(a, b, c)