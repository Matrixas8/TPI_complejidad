from math import ceil

print("hola mundo")

def organizar_estudio_dinamica(n,duration,names,D):
    planner = []
    for _ in range(n+1): planner.append([0]*(D+1))

    for i in range(1,n+1): planner[i][0] = duration[i-1]

    for i in range(D+1): planner[0][i] = i

    tot_hours = 0
    for i in range(n): tot_hours += duration[i] 
    avg_hours = ceil(tot_hours/D)

    for j in range(1,D+1):
        max_pos = 0
        max_hours = 0

        for k in range(1,n+1):
            if planner[k][j-1] > max_hours:
                max_hours = planner[k][j-1]
                max_pos = k
        
        for k in range(1,n+1):
            if k != max_pos:
                planner[k][j] = planner[k][j-1]
            else:
                if (planner[k][j-1] - avg_hours) < 0:
                    planner[k][j] = 0
                else:
                    planner[k][j] = planner[k][j-1] - avg_hours

    planner2 = {}

    for j in range(1,D+1):
        for i in range(1,n+1):
            if planner[i][j] != planner[i][j-1]:
                planner2[f'Dia {j}'] = {f'{names[i-1]}': planner[i][j-1]-planner[i][j]}
                break

    return planner2 

# Datos de prueba
n = 6
duration = [10, 8, 8, 7, 5, 3]
names = ['Diseño','Base de datos','Complejidad','Economia','Comunicaciones','Planificacion']
D = 10

resultados2 = organizar_estudio_dinamica(n,duration,names,D)

print('Planificacion de estudio:')
for dia,materias in resultados2.items():
    print(f'{dia}:')
    for materia,horas in materias.items():
        print(f'    {materia}: {horas} horas')