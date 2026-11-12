import secrets
import string

def crear_contrasena(longitud):
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    todas_las_opciones = letras_mayusculas + letras_minusculas + numeros + simbolos

    password ="".join(secrets.choice(todas_las_opciones) for _ in range(longitud))
    return password

print("bienvenido al generador de contraseñas seguras!")

largo_deseado = int(input("¿Cuántos caracteres quieres que tenga tu código? (Recomendado: 12 o más): "))

mi_nueva_clave = crear_contrasena(largo_deseado)

print("\n--------------------------------------------")
print(f"Tu contraseña segura generada es:", {mi_nueva_clave})
print("\n--------------------------------------------")
