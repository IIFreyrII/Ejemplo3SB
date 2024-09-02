Calificaciones = []
max_size = 5

for i in range(5):
    x = int(input('Ingrese un número: '))
    Calificaciones.append(x)

if len(Calificaciones) > 2:
	Calificaciones.pop(2)

print('Las calificaciones son: ',Calificaciones)
