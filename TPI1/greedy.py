<<<<<<< HEAD
from math import ceils

def organizar_estudio_voraz(n, duration, names, D):
    planner = {}
    tot_hours = 0
    for i in range(n): tot_hours += duration[i] 
    avg_hours = ceil(tot_hours/D)
    
    i = 0 # aumenta los dias
    m = 0 # controla que materia hay que estudiar

    while i<D and any(duration):
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
                m = (m+1)%n
    return planner  

# Datos de prueba
duration = [10, 8, 8, 7, 5, 3]
names = ['Diseño','Base de datos','Complejidad','Economia','Comunicaciones','Planificacion']
D = 10

resultados = organizar_estudio_voraz(len(names),duration,names,D)

if any(duration):
  print("No hay dias suficientes para alcanzar el objetivo")
else:
  print('Planificacion de estudio:')
  for dia,materias in resultados.items():
      print(f'{dia}:')
      for materia,horas in materias.items():
=======
from math import ceil

def organizar_estudio_voraz(n, duration, names, D):
    planner = {}
    tot_hours = 0
    for i in range(n): tot_hours += duration[i] 
    avg_hours = ceil(tot_hours/D)
    
    i = 0 # aumenta los dias
    m = 0 # controla que materia hay que estudiar

    while i<D and any(duration):
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
                m = (m+1)%n
    return planner  

# Datos de prueba
duration = [10, 8, 8, 7, 5, 3]
names = ['Diseño','Base de datos','Complejidad','Economia','Comunicaciones','Planificacion']
D = 10

resultados = organizar_estudio_voraz(len(names),duration,names,D)

if any(duration):
  print("No hay dias suficientes para alcanzar el objetivo")
else:
  print('Planificacion de estudio:')
  for dia,materias in resultados.items():
      print(f'{dia}:')
      for materia,horas in materias.items():
>>>>>>> 9e15d836daaf5f02ae6a7a0c5ce5c39d02c89d37
          print(f'    {materia}: {horas} horas')