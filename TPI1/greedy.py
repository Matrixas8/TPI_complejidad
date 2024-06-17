from math import ceil

def organizar_estudio_voraz(n, duration, names, D):
    planner = {}
    tot_hours = 0
    tot_hours = sum(duration) # Cantidad de horas qeu lleva estudiar todas las materias
    avg_hours = ceil(tot_hours/D) # Cantidad de horas por día
    
    i = 0 # aumenta los dias
    #d = 0 # controla que no se pase de dias
    #t = 0 # controla las materias que ya cumplieron con las horas necesarias
    m = 0 # controla que materia hay que estudiar

    while i < D and any(duration):
        if duration[m] >= avg_hours:
            planner[f'Dia {i+1}'] = {names[m]:avg_hours}
            duration[m] -= avg_hours
            
            if (m+1)<n:
                if duration[m+1] > duration[m]:
                    m += 1
            else:
               m = 0
            
            i += 1
            
        else:
            if duration[m] > 0:
                planner[f'Dia {i+1}'] = {names[m]:duration[m]}
                duration[m] = 0
                i += 1
            else:
                m = (m + 1) % n

#        t = 0
#        for j in range(n):
#            if duration[j] == 0:
#                t += 1
        
    return planner  

# Datos de prueba
n = 6 # Cantidad de materias
duration = [10, 8, 8, 7, 5, 3] # Duraciónen horas de cada materia
names = ['Diseño','Base de datos','Complejidad','Economia','Comunicaciones','Planificacion'] #materias
D = 10 # Cantidad de dias disponibles

resultados = organizar_estudio_voraz(n,duration,names,D)

print('Planificacion de estudio:')
for dia,materias in resultados.items():
    print(f'{dia}:')
    for materia,horas in materias.items():
        print(f'    {materia}: {horas} horas')

