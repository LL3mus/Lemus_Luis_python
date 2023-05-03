#Esta es la primera parte del primer ejercicio

nombre = input('¿Cuál es tu nombre?: ')
apellido_paterno = input('¿Cuál es tu primer apellido?: ')
apellido_materno = input('¿Cuál es tu segundo apellido?: ')
año = input('¿En qué año naciste?: ')
mes_dia = input('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”): ')

#Print de respuestas primera parte

print("1.", nombre)
print("2.", apellido_paterno)
print("3.", apellido_materno)
print("4.", año)
print("5.", mes_dia)

#Esta linea divide la primera parte de la segunda parte del ejercicio 

print("----------------------------------------------")

#Esta es la segunda parte del primer ejercicio

nombre_completo = ("Luis Lemus Bernal")
nombre_upper = nombre_completo.lower()
nombre_lower = nombre_completo.upper()
año_actual = 2023
edad = int(año_actual) - int(año)
suma_edad = sum({edad},10)
media_edad1 = (edad) / 2
media_edad2 = sum({edad},10) / 2

#Contador de letras

letras = nombre_completo
contador1 = 0

for i in letras:
    contador1+=1

#Contador de vocales

vocal = ["a","e","i","o","u"]
contador2 = 0

for i in vocal:
    for j in nombre_completo:
        if (i==j):
            contador2+=1

#Print de respuestas segunda parte

print(f"A. Este es tu nombre completo en mayúsculas: {nombre_upper}")
print(f"B. Este es tu nombre completo en minúsculas: {nombre_lower}")
print(f"C. Esta es tu fecha de nacimiento: {mes_dia}-{año}")
print(f"D. Esta es tu edad: {edad}")
print(f"E. Tu nombre completo tiene", contador2, "vocales.")
print(f"F. Tu nombre completo tiene", contador1, "letras.")

#validacion de interger

x = edad

if isinstance(x,int):
    print("G. ¿Tu edad es un carácter de tipo número?: True")
else:
    print("G. ¿Tu edad es un carácter de tipo número?: False")

#validacion de interger end

#validacion de string
import re

def validar_palabra(palabra):
    patron2 = '^[a-zA-Z0-9_]+$'

    return bool(re.search(patron2, palabra))

texto2 = nombre
print(f"H. ¿Tu nombre completo es un carácter de tipo alfanumérico?: {validar_palabra(texto2)}")

#validacion de string end

print(f"I. Tu edad en 10 años será: {suma_edad}")
print(f"J. La media de tu edad actual y tu edad en 20 años es: {round(media_edad1)} y {round(media_edad2)}")

