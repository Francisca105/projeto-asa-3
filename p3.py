from pulp import *

# Input melhorado
num_brinquedos, num_pacotes, max_valor = map(int, input().split())
brinquedos = [list(map(int, input().split())) for _ in range(num_brinquedos)]
pacotes = [list(map(int, input().split())) for _ in range(num_pacotes)]

# Problema
prob = LpProblem("Problema", LpMaximize)

# Variaveis
vars_brinquedos = [LpVariable(f"x{i+1}", 0, brinquedo[1], LpInteger) for i, brinquedo in enumerate(brinquedos)]
vars_pacotes = [LpVariable(f"y{i+1}", 0, min(brinquedos[pacote[0]-1][1] for pacote in pacotes[i:i+1]), LpInteger) for i in range(num_pacotes)]


# Objetivo
prob += lpDot([brinquedo[0] for brinquedo in brinquedos], vars_brinquedos) + lpDot([pacote[3] for pacote in pacotes], vars_pacotes)

# Restricoes das capacidades de producao de cada brinquedo
for i in range(num_brinquedos):
    indices_pacotes = [j for j, pacote in enumerate(pacotes) if i+1 in pacote[:3]]
    prob += lpSum(vars_pacotes[k] for k in indices_pacotes) + vars_brinquedos[i] <= brinquedos[i][1]

# Restricoes do numero de diferentes brinquedos passiveis de serem produzidos
prob += lpSum(vars_brinquedos) + 3 * lpSum(vars_pacotes) <= max_valor

# Resolucao
prob.writeLP("p3.lp")
prob.solve(GLPK(msg=0))

print(int(value(prob.objective)))