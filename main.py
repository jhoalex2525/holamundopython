# Comentario de línea

'''
Comentario de bloque
'''

#SALIDA POR CONSOLA
print("Hola mundo")

#VARIABLES O ENTRADAS
nombreUsuario = 'Jhony'
edad = 32
estatura = 1.80
escasado = False

#SALIDA
print(nombreUsuario)
print('Buenos días',nombreUsuario)
print(f'Buenos días {nombreUsuario}')
print(f'Buenos días {nombreUsuario}, su edad es {edad} y mides {estatura}. ¿Tu estado civil es casado? {escasado}')

#RECIBIENDO VARIABLES DESDE LA CONSOLA
numero1 = input('Digite un número entero: ') + input('Digite un segundo número entero: ')
print(f'Usted digitó el número {numero1}')

#RECIBIENDO VARIABLES DESDE LA CONSOLA
numero1 = int(input('Digite un número entero: '))+int(input('Digite un segundo número entero: '))
print(f'La suma de los números es {numero1}')