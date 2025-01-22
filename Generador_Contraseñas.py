import random
import string

def generar_contraseña(longitud, incluir_caracteres_especiales=True, incluir_numeros=True, incluir_mayusculas=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

def main():
    print(generar_contraseña(10))
    print(generar_contraseña(10, incluir_numeros=False))
    print(generar_contraseña(10, incluir_mayusculas=False))
    print(generar_contraseña(10, incluir_caracteres_especiales=False))
    print(generar_contraseña(10, incluir_caracteres_especiales=False, incluir_numeros=False, incluir_mayusculas=False))


if __name__ == '__main__':
    main()