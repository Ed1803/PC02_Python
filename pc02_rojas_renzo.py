
# Pregunta 1
for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        print("El número", numero, "es divisible por 7 y múltiplo de 5")

# Pregunta 2
n = int(input("Ingrese un numero:"))
# Parte superior
for i in range(1, n + 1):
    print('* ' * i)
# Parte inferior
for i in range(n - 1, 0, -1):
    print('* ' * i)

#Pregunta3

numeros = []
numeros_pares = []
numeros_impares = []

while True:
    respuesta = input("¿Desea ingresar un numero? (SI/NO): ").upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
             numeros_impares.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("ERROR. Ingrese nuevamente.")

print("Numeros ingresados:", numeros)
print("Cantidad de numeros pares:", len(numeros_pares))
print("Cantidad de numeros impares:", len(numeros_impares))

#Pregunta 4
lista_alumnos = []
n = int(input("Ingrese el número de alumnos: "))

for i in range(n):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas_alumno = []

    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1} para {nombre_alumno}: "))
        #Uso de listas
        notas_alumno.append(calificacion)
     # Uso de diccionarios
    alumno_info = {"Alumno": nombre_alumno, "Notas": notas_alumno}
    lista_alumnos.append(alumno_info)

print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)

# Pregunta 5
def contar_digitos(numero, digito):
    # Convertir el número a una cadena para utilizar el método count()
    numero_str = str(numero)
    # Contar la cantidad de veces que aparece el dígito en el número
    ctd = numero_str.count(str(digito))
    print(f"Cantidad de veces {digito} en el numero {numero} es: {ctd}")


numero_ingre = int(input("Ingrese un numero: "))
digito_contar = int(input("Ingrese un digito de ese numero: "))
contar_digitos(numero_ingre, digito_contar)

#Pregunta 6
def fibonacci(limite):
    a, b = 0, 1
    fibonacci_series = [a, b]

    while b < limite:
        a, b = b, a + b
        fibonacci_series.append(b)
    return fibonacci_series

limite = int(input("Ingrese el limite de la serie Fibonaaci: "))
serie_fibonacci = fibonacci(limite)
print("La Serie de Fibonacci hasta", limite, "es :", serie_fibonacci)

#Pregunta 7
def esprimo(numero):
    count = 0
    for i in range(1, numero + 1):
        a = numero % i
        if a == 0:
            count = count + 1
    if count == 2:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

numero_ev = int(input("Ingrese un número para verificar si es primo: "))
esprimo(numero_ev)

#Pregunta 8
def calcule_factorial(f):
    if f == 0:
        return 1
    else:
        return f * calcule_factorial(f - 1)

while True:
    factorial = int(input("Ingrese el número para calcular el factorial: "))

    if factorial >= 0:
        break
    else:
        print("Por favor, ingrese un número no negativo.")

resultado = calcule_factorial(factorial)
print(f"El factorial de {factorial} es: {resultado}")

# Pregunta 9
def omitir_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cadena_sin_vocales = ""

    for letra in cadena:
        # Verificar si el caracter no es una vocal
        if letra not in vocales:
            # Agregar el caracter a la cadena resultante
            cadena_sin_vocales += letra

    return cadena_sin_vocales

# Solicitar al usuario una cadena de texto
entrada_usuario = input("Ingrese una cadena de texto: ")
resultado = omitir_vocales(entrada_usuario)
print("Cadena original:", entrada_usuario)
print("Cadena sin vocales:", resultado)

def convertir_fecha(input_fecha):
    meses = {
        "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
        "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
    }

    # Dividir la entrada en palabras
    datos = input_fecha.split()

    # Verificar si la entrada tiene formato mes-día-año
    if '/' in input_fecha:
        mes, dia, año = map(int, input_fecha.split('/'))
    else:
        # Obtener mes, día y año de la entrada con nombres de meses
        mes = meses[datos[0]]
        dia = int(datos[1].replace(',', ''))
        año = int(datos[2])

    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = f"{año:04d}-{mes:02d}-{dia:02d}"
    print(f"Input: {input_fecha} | Output: {fecha_formateada}")


# Ejemplos
convertir_fecha("9/8/1636")
convertir_fecha("Septiembre 8, 1636")
convertir_fecha("1/1/1970")
