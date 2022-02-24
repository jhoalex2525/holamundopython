# # Comentario de línea

# '''
# Comentario de bloque
# '''

# #SALIDA POR CONSOLA
# print("Hola mundo")

# #VARIABLES O ENTRADAS
# nombreUsuario = 'Jhony'
# edad = 32
# estatura = 1.80
# escasado = False

# #SALIDA
# print(nombreUsuario)
# print('Buenos días',nombreUsuario)
# print(f'Buenos días {nombreUsuario}')
# print(f'Buenos días {nombreUsuario}, su edad es {edad} y mides {estatura}. ¿Tu estado civil es casado? {escasado}')

# #RECIBIENDO VARIABLES DESDE LA CONSOLA
# numero1 = input('Digite un número entero: ') + input('Digite un segundo número entero: ')
# print(f'Usted digitó el número {numero1}')

# #RECIBIENDO VARIABLES DESDE LA CONSOLA
# numero1 = int(input('Digite un número entero: '))+int(input('Digite un segundo número entero: '))
# print(f'La suma de los números es {numero1}')

#                                                   24 02 2022
#                                               TOMANDO DECISIONES
#                                           Ejemplo1: numero + o -
# numero1 = int(input('Digite un número: '))
# print(f'El número digitado es: {numero1}')
# if(numero1>=0):
#     print('El número es positivo')
# else:
#     print('El número es negativo')

#                                            Ejemplo2: Hidrotuango
# nivelAgua = int(input('Digite el nivel de agua: '))
# if(nivelAgua<200):
#     print('Alerta, hay poca agua')
# elif(nivelAgua>=200 and nivelAgua<450):
#     print('El nivel de agua es adecuado')
# else:
#     print('Peligro, exceso de agua')

#                                             Ejemplo3.1: Estaciones con numero
# numeroMes = int(input('Digite el número del mes: '))
# if(numeroMes<=0):
#     print('Digite un número correcto')
# elif(numeroMes<4):
#     print('La estación es Invierno')
# elif(numeroMes<7):
#     print('La estación es Verano')
# elif(numeroMes<10):
#     print('La estación es Otoño')
# elif(numeroMes<13):
#     print('La estación es Primavera')
# else:
#     print('El número de mes digitado no es válido')

#                                           Ejemplo3.2: Estaciones con Texto
# mes = str(input('Digite el nombre completo del mes y en minuscula: ')).lower()
# if(mes == 'enero' or mes == 'febrero' or mes == 'marzo'):
#     print('La estación es Invierno')
# elif(mes == 'abril' or mes == 'mayo' or mes == 'junio'):
#     print('La estación es Verano')
# elif(mes == 'julio' or mes == 'agosto' or mes == 'septiembre'):
#     print('La estación es Otoño')
# elif(mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre'):
#     print('La estación es Primavera')
# else:
#     print('El mes digitado no es válido')

#                                                   BUCLES

# contador = 0
# while(contador<10):
#     contador+=1
#     print(contador)
# else:
#     print('Terminó el ciclo')

contador = 0
suma = 0
while(contador>=0):
    suma+=contador
    contador = int(input("Digite un número: "))
        
print(f'La suma es: {suma}')