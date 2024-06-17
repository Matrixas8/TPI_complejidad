from math import ceil

def organizar_estudio_dinamica(n,duration,names,D):
    planner = []
    total_materias = True

    # Inicializa matriz en 0
    for _ in range(n + 1):
        planner.append([0] * (D + 1))

    # Inicializa la primer columna con las duración de cada materia
    for i in range(1, n + 1):
        planner[i][0] = duration[i - 1]

    # Inicializa la primer fila con los dias a estudiar
    for i in range(D + 1):
        planner[0][i] = i
    
    tot_hours = 0
    for i in range(n): tot_hours += duration[i] 
    avg_hours = ceil(tot_hours/D)

    for j in range(1,D+1):
        max_pos = 0
        max_hours = 0

        # Busca la materia con mayor duración de cada día
        for k in range(1,n+1):
            if planner[k][j-1] > max_hours:
                max_hours = planner[k][j-1]
                max_pos = k
        
        # Recorre las filas del dia
        for k in range(1,n+1):
            # Si no es la matreia con mayor duración se la deja como esta
            if k != max_pos:
                planner[k][j] = planner[k][j-1]
            else:
                # Sino se descuenta la cantidad de horas diarias
                if (planner[k][j-1] - avg_hours) < 0:
                    planner[k][j] = 0
                else:
                    planner[k][j] = planner[k][j-1] - avg_hours

    # Verifica si todas las materias completaron sus horas de estudio
    for i in range(1, n+1):
        if planner[i][D] != 0:
            total_materias = False
            break
    
    # Se arma la solución
    if total_materias:
        planner2 = {}
        for j in range(1,D+1):
            for i in range(1,n+1):
                if planner[i][j] != planner[i][j-1]:
                    planner2[f'Dia {j}'] = {f'{names[i-1]}': planner[i][j-1]-planner[i][j]}
                    break
    else:
        planner2 = 0

    return planner2 

# Datos de prueba
duration = [10, 8, 8, 7, 5, 3]
names = ['Diseño','Base de datos','Complejidad','Economia','Comunicaciones','Planificacion']
D = 10

resultados2 = organizar_estudio_dinamica(len(names),duration,names,D)

# Muestra de la solució
if resultados2 == 0:
    print("No hay dias suficientes para alcanzar el objetivo")
else:
    print('Planificacion de estudio:')
    for dia,materias in resultados2.items():
        print(f'{dia}:')
        for materia,horas in materias.items():
            print(f'    {materia}: {horas} horas')
