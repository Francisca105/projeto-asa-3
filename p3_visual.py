from pulp import *

# Input
entrada = input()
numeros = [int(numero) for numero in entrada.split()]
num_brinquedos = numeros[0]
num_pacotes = numeros[1]
max = numeros[2]
brinquedos = []
pacotes = []

for i in range(num_brinquedos):
    brinquedo = input()
    brinquedos.append([int(numero) for numero in brinquedo.split()])
for i in range(num_pacotes):
    pacote = input()
    pacotes.append([int(numero) for numero in pacote.split()])

# Problema
prob = LpProblem("Problema", LpMaximize)

# Variaveis
vars_brinquedos = [LpVariable(f"x{i+1}", 0, brinquedos[i][1], LpInteger) for i in range(num_brinquedos)]
vars_pacotes = [LpVariable(f"y{i+1}", 0, min([brinquedos[pacotes[i][0]-1][1], brinquedos[pacotes[i][1]-1][1], brinquedos[pacotes[i][2]-1][1]]), LpInteger) for i in range(num_pacotes)]

# Objetivo
prob += lpSum(brinquedos[i][0] * vars_brinquedos[i] for i in range(num_brinquedos)) + lpSum(pacotes[i][3] * vars_pacotes[i] for i in range(num_pacotes))

# Restricoes das capacidades de producao de cada brinquedo
for i in range(num_brinquedos):
    lista = [0 for i in range(num_pacotes)]
    for j in range(num_pacotes):
        if (i == (pacotes[j][0]-1) or i == (pacotes[j][1]-1) or i == (pacotes[j][2]-1)):
            lista[j] = 1
    prob += vars_brinquedos[i] + lpSum([lista[k]*vars_pacotes[k] for k in range(num_pacotes)]) <= brinquedos[i][1]

# Restricoes do numero de diferentes brinquedos passiveis de serem produzidos
prob += lpSum(vars_brinquedos[i] for i in range(num_brinquedos)) + lpSum(3*vars_pacotes[j] for j in range(num_pacotes)) <= max

# Resolucao
prob.writeLP("p3.lp")

prob.solve()

# Output
for i in range(num_brinquedos):
    print(brinquedos[i])
for i in range(num_pacotes):
    print(pacotes[i])

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("objective = ", prob.objective)

for a in prob.constraints:
    print(prob.constraints[a])

print("objective =", int(value(prob.objective)))
