from pulp import *

# Input
entrada = input()
numeros = [int(numero) for numero in entrada.split()]
t = numeros[0]
p = numeros[1]
max = numeros[2]
brinquedos = []
pacotes = []

for i in range(t):
    brinquedo = input()
    brinquedos.append([int(numero) for numero in brinquedo.split()])
for i in range(p):
    pacote = input()
    pacotes.append([int(numero) for numero in pacote.split()])
    
# Output
for i in range(t):
    print(brinquedos[i])
for i in range(p):
    print(pacotes[i])

# model = LpProblem("UbiquityInc")
# res = LpVariable("res", 0, 1, cat="Integer")

# model += ...

# model.solve()
# print(f"Res:", LpStatus[res.varValue])
