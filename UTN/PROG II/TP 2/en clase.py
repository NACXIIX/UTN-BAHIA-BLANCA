notas = [60, 65, 80, 94, 34, 95, 96, 100]
notas_ajustadas = notas[:]
notas_ajustadas.sort()

for i in range(len(notas_ajustadas)):
    if notas_ajustadas[i] <= 95:
        notas_ajustadas[i] += 5
    if notas_ajustadas[i] > 95 and notas_ajustadas[i] < 100:
        notas_ajustadas[i] = 100
        


for i in range(len(notas_ajustadas)):
    print(f"La nota {i+1} es: {notas_ajustadas[i]}")